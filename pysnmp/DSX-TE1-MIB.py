# SNMP MIB module (DSX-TE1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSX-TE1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:43 2024
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

(nndsxT1E1IfGroup,) = mibBuilder.importSymbols(
    "DSX-TC-MIB",
    "nndsxT1E1IfGroup")

(ntEnterpriseDataTasmanInterfaces,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanInterfaces")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nndsxT1E1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1)
)
nndsxT1E1MIB.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NndsxT1E1IfConfigGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfConfigGroup = _NndsxT1E1IfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1)
)
_NndsxT1E1IfConfigLineTable_Object = MibTable
nndsxT1E1IfConfigLineTable = _NndsxT1E1IfConfigLineTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigLineTable.setStatus("current")
_NndsxT1E1IfConfigLineEntry_Object = MibTableRow
nndsxT1E1IfConfigLineEntry = _NndsxT1E1IfConfigLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1)
)
nndsxT1E1IfConfigLineEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigLineEntry.setStatus("current")
_NndsxT1E1IfIndex_Type = Integer32
_NndsxT1E1IfIndex_Object = MibTableColumn
nndsxT1E1IfIndex = _NndsxT1E1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1),
    _NndsxT1E1IfIndex_Type()
)
nndsxT1E1IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nndsxT1E1IfIndex.setStatus("current")
_NndsxT1E1IfConfigServiceMode_Type = TruthValue
_NndsxT1E1IfConfigServiceMode_Object = MibTableColumn
nndsxT1E1IfConfigServiceMode = _NndsxT1E1IfConfigServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2),
    _NndsxT1E1IfConfigServiceMode_Type()
)
nndsxT1E1IfConfigServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigServiceMode.setStatus("current")


class _NndsxT1E1IfConfigLineMode_Type(Integer32):
    """Custom type nndsxT1E1IfConfigLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linemode-csu", 1),
          ("linemode-dsx", 2))
    )


_NndsxT1E1IfConfigLineMode_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigLineMode_Object = MibTableColumn
nndsxT1E1IfConfigLineMode = _NndsxT1E1IfConfigLineMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 3),
    _NndsxT1E1IfConfigLineMode_Type()
)
nndsxT1E1IfConfigLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigLineMode.setStatus("current")


class _NndsxT1E1IfConfigLineType_Type(Integer32):
    """Custom type nndsxT1E1IfConfigLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("linetype-d4", 3),
          ("linetype-e1crcmf", 5),
          ("linetype-e1mf", 6),
          ("linetype-e1unframed", 7),
          ("linetype-esf", 2))
    )


_NndsxT1E1IfConfigLineType_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigLineType_Object = MibTableColumn
nndsxT1E1IfConfigLineType = _NndsxT1E1IfConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 4),
    _NndsxT1E1IfConfigLineType_Type()
)
nndsxT1E1IfConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigLineType.setStatus("current")


class _NndsxT1E1IfConfigLineCode_Type(Integer32):
    """Custom type nndsxT1E1IfConfigLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("linecode-ami", 5),
          ("linecode-b8zs", 2),
          ("linecode-hdb3", 3))
    )


_NndsxT1E1IfConfigLineCode_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigLineCode_Object = MibTableColumn
nndsxT1E1IfConfigLineCode = _NndsxT1E1IfConfigLineCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 5),
    _NndsxT1E1IfConfigLineCode_Type()
)
nndsxT1E1IfConfigLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigLineCode.setStatus("current")


class _NndsxT1E1IfConfigLBO_Type(Integer32):
    """Custom type nndsxT1E1IfConfigLBO based on Integer32"""
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
        *(("lbo-12-db", 5),
          ("lbo-15-db", 3),
          ("lbo-225-db", 4),
          ("lbo-43-db", 6),
          ("lbo-75-db", 2),
          ("lbo-zero-db", 1))
    )


_NndsxT1E1IfConfigLBO_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigLBO_Object = MibTableColumn
nndsxT1E1IfConfigLBO = _NndsxT1E1IfConfigLBO_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 6),
    _NndsxT1E1IfConfigLBO_Type()
)
nndsxT1E1IfConfigLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigLBO.setStatus("current")


class _NndsxT1E1IfConfigCableLength_Type(Integer32):
    """Custom type nndsxT1E1IfConfigCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cable-length-0-133-or-0-110", 1),
          ("cable-length-133-266-or-110-220", 2),
          ("cable-length-266-399-or-220-330", 3),
          ("cable-length-399-533-or-330-440", 4),
          ("cable-length-533-655-or-440-550", 5),
          ("cable-length-550-660", 6),
          ("cable-length-none", 0))
    )


_NndsxT1E1IfConfigCableLength_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigCableLength_Object = MibTableColumn
nndsxT1E1IfConfigCableLength = _NndsxT1E1IfConfigCableLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 7),
    _NndsxT1E1IfConfigCableLength_Type()
)
nndsxT1E1IfConfigCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigCableLength.setStatus("current")


class _NndsxT1E1IfConfigRaiAlarm_Type(Integer32):
    """Custom type nndsxT1E1IfConfigRaiAlarm based on Integer32"""
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
        *(("rai-det-enable", 2),
          ("rai-disable", 4),
          ("rai-gen-det-enable", 3),
          ("rai-gen-enable", 1))
    )


_NndsxT1E1IfConfigRaiAlarm_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigRaiAlarm_Object = MibTableColumn
nndsxT1E1IfConfigRaiAlarm = _NndsxT1E1IfConfigRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 8),
    _NndsxT1E1IfConfigRaiAlarm_Type()
)
nndsxT1E1IfConfigRaiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigRaiAlarm.setStatus("current")


class _NndsxT1E1IfConfigTransmitClock_Type(Integer32):
    """Custom type nndsxT1E1IfConfigTransmitClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timing-backplane", 3),
          ("timing-internal", 2),
          ("timing-line", 1))
    )


_NndsxT1E1IfConfigTransmitClock_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigTransmitClock_Object = MibTableColumn
nndsxT1E1IfConfigTransmitClock = _NndsxT1E1IfConfigTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 9),
    _NndsxT1E1IfConfigTransmitClock_Type()
)
nndsxT1E1IfConfigTransmitClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigTransmitClock.setStatus("current")


class _NndsxT1E1IfConfigTimeSlotMap_Type(OctetString):
    """Custom type nndsxT1E1IfConfigTimeSlotMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NndsxT1E1IfConfigTimeSlotMap_Type.__name__ = "OctetString"
_NndsxT1E1IfConfigTimeSlotMap_Object = MibTableColumn
nndsxT1E1IfConfigTimeSlotMap = _NndsxT1E1IfConfigTimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 10),
    _NndsxT1E1IfConfigTimeSlotMap_Type()
)
nndsxT1E1IfConfigTimeSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigTimeSlotMap.setStatus("current")


class _NndsxT1E1IfConfigCableType_Type(Integer32):
    """Custom type nndsxT1E1IfConfigCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cable-type-coax", 1),
          ("cable-type-none", 0),
          ("cable-type-twistedpair", 2))
    )


_NndsxT1E1IfConfigCableType_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigCableType_Object = MibTableColumn
nndsxT1E1IfConfigCableType = _NndsxT1E1IfConfigCableType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 11),
    _NndsxT1E1IfConfigCableType_Type()
)
nndsxT1E1IfConfigCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigCableType.setStatus("current")


class _NndsxT1E1IfCircuitId_Type(DisplayString):
    """Custom type nndsxT1E1IfCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NndsxT1E1IfCircuitId_Type.__name__ = "DisplayString"
_NndsxT1E1IfCircuitId_Object = MibTableColumn
nndsxT1E1IfCircuitId = _NndsxT1E1IfCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 12),
    _NndsxT1E1IfCircuitId_Type()
)
nndsxT1E1IfCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfCircuitId.setStatus("current")


class _NndsxT1E1IfContactInfo_Type(DisplayString):
    """Custom type nndsxT1E1IfContactInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NndsxT1E1IfContactInfo_Type.__name__ = "DisplayString"
_NndsxT1E1IfContactInfo_Object = MibTableColumn
nndsxT1E1IfContactInfo = _NndsxT1E1IfContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 13),
    _NndsxT1E1IfContactInfo_Type()
)
nndsxT1E1IfContactInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfContactInfo.setStatus("current")


class _NndsxT1E1IfDescription_Type(DisplayString):
    """Custom type nndsxT1E1IfDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 76),
    )


_NndsxT1E1IfDescription_Type.__name__ = "DisplayString"
_NndsxT1E1IfDescription_Object = MibTableColumn
nndsxT1E1IfDescription = _NndsxT1E1IfDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 14),
    _NndsxT1E1IfDescription_Type()
)
nndsxT1E1IfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfDescription.setStatus("current")


class _NndsxT1E1IfConfigJitter_Type(Integer32):
    """Custom type nndsxT1E1IfConfigJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jitter-disable", 1),
          ("jitter-enable", 2),
          ("jitter-none", 0))
    )


_NndsxT1E1IfConfigJitter_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigJitter_Object = MibTableColumn
nndsxT1E1IfConfigJitter = _NndsxT1E1IfConfigJitter_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 15),
    _NndsxT1E1IfConfigJitter_Type()
)
nndsxT1E1IfConfigJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigJitter.setStatus("current")
_NndsxT1E1IfConfigAlarmHierarchy_Type = TruthValue
_NndsxT1E1IfConfigAlarmHierarchy_Object = MibTableColumn
nndsxT1E1IfConfigAlarmHierarchy = _NndsxT1E1IfConfigAlarmHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 1, 1, 16),
    _NndsxT1E1IfConfigAlarmHierarchy_Type()
)
nndsxT1E1IfConfigAlarmHierarchy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigAlarmHierarchy.setStatus("current")
_NndsxT1E1IfConfigFdlTable_Object = MibTable
nndsxT1E1IfConfigFdlTable = _NndsxT1E1IfConfigFdlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigFdlTable.setStatus("current")
_NndsxT1E1IfConfigFdlEntry_Object = MibTableRow
nndsxT1E1IfConfigFdlEntry = _NndsxT1E1IfConfigFdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigFdlEntry.setStatus("current")


class _NndsxT1E1IfConfigFdl_Type(Integer32):
    """Custom type nndsxT1E1IfConfigFdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fdl-ansi-att", 3),
          ("fdl-ansi-only", 1),
          ("fdl-att-only", 2))
    )


_NndsxT1E1IfConfigFdl_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigFdl_Object = MibTableColumn
nndsxT1E1IfConfigFdl = _NndsxT1E1IfConfigFdl_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1),
    _NndsxT1E1IfConfigFdl_Type()
)
nndsxT1E1IfConfigFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigFdl.setStatus("current")


class _NndsxT1E1IfConfigFdlCsuDsuType_Type(Integer32):
    """Custom type nndsxT1E1IfConfigFdlCsuDsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fdl-csu", 1),
          ("fdl-csudsu", 3),
          ("fdl-dsu", 2))
    )


_NndsxT1E1IfConfigFdlCsuDsuType_Type.__name__ = "Integer32"
_NndsxT1E1IfConfigFdlCsuDsuType_Object = MibTableColumn
nndsxT1E1IfConfigFdlCsuDsuType = _NndsxT1E1IfConfigFdlCsuDsuType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2),
    _NndsxT1E1IfConfigFdlCsuDsuType_Type()
)
nndsxT1E1IfConfigFdlCsuDsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfConfigFdlCsuDsuType.setStatus("current")
_NndsxT1E1IfAlarmConfigGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfAlarmConfigGroup = _NndsxT1E1IfAlarmConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3)
)
_NndsxT1E1IfAlarmThresholdConfigTable_Object = MibTable
nndsxT1E1IfAlarmThresholdConfigTable = _NndsxT1E1IfAlarmThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigTable.setStatus("current")
_NndsxT1E1IfAlarmThresholdConfigEntry_Object = MibTableRow
nndsxT1E1IfAlarmThresholdConfigEntry = _NndsxT1E1IfAlarmThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1)
)
nndsxT1E1IfAlarmThresholdConfigEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfAlarmThresholdConfigIndex"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigEntry.setStatus("current")
_NndsxT1E1IfAlarmThresholdConfigIndex_Type = Integer32
_NndsxT1E1IfAlarmThresholdConfigIndex_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigIndex = _NndsxT1E1IfAlarmThresholdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1),
    _NndsxT1E1IfAlarmThresholdConfigIndex_Type()
)
nndsxT1E1IfAlarmThresholdConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigIndex.setStatus("current")


class _NndsxT1E1IfAlarmThresholdConfigObject_Type(Integer32):
    """Custom type nndsxT1E1IfAlarmThresholdConfigObject based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("te1-object-bes", 4),
          ("te1-object-bpv", 8),
          ("te1-object-crc", 10),
          ("te1-object-css", 7),
          ("te1-object-eev", 1),
          ("te1-object-es", 2),
          ("te1-object-lofc", 6),
          ("te1-object-none", 0),
          ("te1-object-oof", 9),
          ("te1-object-ses", 5),
          ("te1-object-uas", 3))
    )


_NndsxT1E1IfAlarmThresholdConfigObject_Type.__name__ = "Integer32"
_NndsxT1E1IfAlarmThresholdConfigObject_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigObject = _NndsxT1E1IfAlarmThresholdConfigObject_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 2),
    _NndsxT1E1IfAlarmThresholdConfigObject_Type()
)
nndsxT1E1IfAlarmThresholdConfigObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigObject.setStatus("current")


class _NndsxT1E1IfAlarmThresholdConfigSamplingInterval_Type(Integer32):
    """Custom type nndsxT1E1IfAlarmThresholdConfigSamplingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NndsxT1E1IfAlarmThresholdConfigSamplingInterval_Type.__name__ = "Integer32"
_NndsxT1E1IfAlarmThresholdConfigSamplingInterval_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigSamplingInterval = _NndsxT1E1IfAlarmThresholdConfigSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 3),
    _NndsxT1E1IfAlarmThresholdConfigSamplingInterval_Type()
)
nndsxT1E1IfAlarmThresholdConfigSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigSamplingInterval.setStatus("current")


class _NndsxT1E1IfAlarmThresholdConfigSampleType_Type(Integer32):
    """Custom type nndsxT1E1IfAlarmThresholdConfigSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sample-absolute", 1),
          ("sample-delta", 2))
    )


_NndsxT1E1IfAlarmThresholdConfigSampleType_Type.__name__ = "Integer32"
_NndsxT1E1IfAlarmThresholdConfigSampleType_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigSampleType = _NndsxT1E1IfAlarmThresholdConfigSampleType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 4),
    _NndsxT1E1IfAlarmThresholdConfigSampleType_Type()
)
nndsxT1E1IfAlarmThresholdConfigSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigSampleType.setStatus("current")
_NndsxT1E1IfAlarmThresholdConfigRisingThreshold_Type = Integer32
_NndsxT1E1IfAlarmThresholdConfigRisingThreshold_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigRisingThreshold = _NndsxT1E1IfAlarmThresholdConfigRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 5),
    _NndsxT1E1IfAlarmThresholdConfigRisingThreshold_Type()
)
nndsxT1E1IfAlarmThresholdConfigRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigRisingThreshold.setStatus("current")
_NndsxT1E1IfAlarmThresholdConfigFallingThreshold_Type = Integer32
_NndsxT1E1IfAlarmThresholdConfigFallingThreshold_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigFallingThreshold = _NndsxT1E1IfAlarmThresholdConfigFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 6),
    _NndsxT1E1IfAlarmThresholdConfigFallingThreshold_Type()
)
nndsxT1E1IfAlarmThresholdConfigFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigFallingThreshold.setStatus("current")
_NndsxT1E1IfAlarmThresholdConfigEnable_Type = TruthValue
_NndsxT1E1IfAlarmThresholdConfigEnable_Object = MibTableColumn
nndsxT1E1IfAlarmThresholdConfigEnable = _NndsxT1E1IfAlarmThresholdConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 7),
    _NndsxT1E1IfAlarmThresholdConfigEnable_Type()
)
nndsxT1E1IfAlarmThresholdConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmThresholdConfigEnable.setStatus("current")
_NndsxT1E1IfTestConfigTable_Object = MibTable
nndsxT1E1IfTestConfigTable = _NndsxT1E1IfTestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfTestConfigTable.setStatus("current")
_NndsxT1E1IfTestConfigEntry_Object = MibTableRow
nndsxT1E1IfTestConfigEntry = _NndsxT1E1IfTestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfTestConfigEntry.setStatus("current")


class _NndsxT1E1IfTestConfigType_Type(Integer32):
    """Custom type nndsxT1E1IfTestConfigType based on Integer32"""
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
        *(("inward1-analog-loopback-test", 7),
          ("inward1-loopback-test", 6),
          ("inward2-loopback-test", 8),
          ("line-local-loopback-test", 5),
          ("line-loopback-test", 3),
          ("local-loopback-test", 4),
          ("no-test", 1),
          ("pattern-test", 9),
          ("payload-loopback-test", 2),
          ("remote-lpdn-test", 11),
          ("remote-lpup-test", 10))
    )


_NndsxT1E1IfTestConfigType_Type.__name__ = "Integer32"
_NndsxT1E1IfTestConfigType_Object = MibTableColumn
nndsxT1E1IfTestConfigType = _NndsxT1E1IfTestConfigType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1, 1),
    _NndsxT1E1IfTestConfigType_Type()
)
nndsxT1E1IfTestConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestConfigType.setStatus("current")
_NndsxT1E1IfTestConfigTime_Type = Unsigned32
_NndsxT1E1IfTestConfigTime_Object = MibTableColumn
nndsxT1E1IfTestConfigTime = _NndsxT1E1IfTestConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1, 2),
    _NndsxT1E1IfTestConfigTime_Type()
)
nndsxT1E1IfTestConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestConfigTime.setStatus("current")


class _NndsxT1E1IfTestConfigPattern_Type(Integer32):
    """Custom type nndsxT1E1IfTestConfigPattern based on Integer32"""
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
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("pattern-1in3", 5),
          ("pattern-1in5", 6),
          ("pattern-1in7", 7),
          ("pattern-211minus1", 21),
          ("pattern-215minus1", 13),
          ("pattern-220minus1", 14),
          ("pattern-223minus1", 16),
          ("pattern-29minus1", 12),
          ("pattern-3in24", 4),
          ("pattern-all-ones", 1),
          ("pattern-all-zeros", 2),
          ("pattern-alt-resetcod", 20),
          ("pattern-alt-setcode", 19),
          ("pattern-alternating", 3),
          ("pattern-none", 0),
          ("pattern-qrw", 15),
          ("pattern-smartjack-lpdown", 9),
          ("pattern-smartjack-lpup", 8),
          ("pattern-std-resetcod", 18),
          ("pattern-std-setcode", 17),
          ("pattern-user1", 10),
          ("pattern-user2", 11))
    )


_NndsxT1E1IfTestConfigPattern_Type.__name__ = "Integer32"
_NndsxT1E1IfTestConfigPattern_Object = MibTableColumn
nndsxT1E1IfTestConfigPattern = _NndsxT1E1IfTestConfigPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1, 3),
    _NndsxT1E1IfTestConfigPattern_Type()
)
nndsxT1E1IfTestConfigPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestConfigPattern.setStatus("current")


class _NndsxT1E1IfTestConfigLoopCode_Type(Integer32):
    """Custom type nndsxT1E1IfTestConfigLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("loopcode-line-alternate", 3),
          ("loopcode-line-ansiFDL", 4),
          ("loopcode-line-standard", 2),
          ("loopcode-none", 1),
          ("loopcode-payload-ATTFDL", 6),
          ("loopcode-payload-ansiFDL", 7),
          ("loopcode-smartjack", 9),
          ("loopcode-v54", 8))
    )


_NndsxT1E1IfTestConfigLoopCode_Type.__name__ = "Integer32"
_NndsxT1E1IfTestConfigLoopCode_Object = MibTableColumn
nndsxT1E1IfTestConfigLoopCode = _NndsxT1E1IfTestConfigLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1, 4),
    _NndsxT1E1IfTestConfigLoopCode_Type()
)
nndsxT1E1IfTestConfigLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestConfigLoopCode.setStatus("current")


class _NndsxT1E1IfMonitorPortConfigType_Type(Integer32):
    """Custom type nndsxT1E1IfMonitorPortConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor-enable", 2),
          ("monitor-none", 1))
    )


_NndsxT1E1IfMonitorPortConfigType_Type.__name__ = "Integer32"
_NndsxT1E1IfMonitorPortConfigType_Object = MibTableColumn
nndsxT1E1IfMonitorPortConfigType = _NndsxT1E1IfMonitorPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1, 5),
    _NndsxT1E1IfMonitorPortConfigType_Type()
)
nndsxT1E1IfMonitorPortConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nndsxT1E1IfMonitorPortConfigType.setStatus("current")


class _NndsxT1E1IfMonitorPortTxInjectType_Type(Integer32):
    """Custom type nndsxT1E1IfMonitorPortTxInjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inject-none", 1),
          ("inject-sendtype", 2))
    )


_NndsxT1E1IfMonitorPortTxInjectType_Type.__name__ = "Integer32"
_NndsxT1E1IfMonitorPortTxInjectType_Object = MibTableColumn
nndsxT1E1IfMonitorPortTxInjectType = _NndsxT1E1IfMonitorPortTxInjectType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 1, 4, 1, 6),
    _NndsxT1E1IfMonitorPortTxInjectType_Type()
)
nndsxT1E1IfMonitorPortTxInjectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nndsxT1E1IfMonitorPortTxInjectType.setStatus("current")
_NndsxT1E1IfStatusGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfStatusGroup = _NndsxT1E1IfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2)
)
_NndsxT1E1IfStatusTable_Object = MibTable
nndsxT1E1IfStatusTable = _NndsxT1E1IfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfStatusTable.setStatus("current")
_NndsxT1E1IfStatusEntry_Object = MibTableRow
nndsxT1E1IfStatusEntry = _NndsxT1E1IfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfStatusEntry.setStatus("current")


class _NndsxT1E1IfStatusLineStatus_Type(Bits):
    """Custom type nndsxT1E1IfStatusLineStatus based on Bits"""
    namedValues = NamedValues(
        *(("loopbackStatus", 24),
          ("lorcStatus", 10),
          ("raisStatus", 28),
          ("rcvTestCode", 20),
          ("reserved1", 0),
          ("reserved10", 22),
          ("reserved11", 23),
          ("reserved12", 25),
          ("reserved13", 26),
          ("reserved14", 29),
          ("reserved15", 31),
          ("reserved2", 1),
          ("reserved3", 7),
          ("reserved4", 8),
          ("reserved5", 9),
          ("reserved6", 12),
          ("reserved7", 13),
          ("reserved8", 19),
          ("reserved9", 21),
          ("rexzStatus", 6),
          ("risStatus", 5),
          ("rlofStatus", 30),
          ("rlosStatus", 4),
          ("rraiStatus", 2),
          ("sendLineCode", 14),
          ("sendPattern", 18),
          ("sendPayLoadCode", 15),
          ("sendResetCode", 16),
          ("sendTE1Code", 17),
          ("taisStatus", 27),
          ("tpdeStatus", 11),
          ("traiStatus", 3))
    )

_NndsxT1E1IfStatusLineStatus_Type.__name__ = "Bits"
_NndsxT1E1IfStatusLineStatus_Object = MibTableColumn
nndsxT1E1IfStatusLineStatus = _NndsxT1E1IfStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1),
    _NndsxT1E1IfStatusLineStatus_Type()
)
nndsxT1E1IfStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfStatusLineStatus.setStatus("current")


class _NndsxT1E1IfStatusTransmitClock_Type(Integer32):
    """Custom type nndsxT1E1IfStatusTransmitClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timing-internal", 2),
          ("timing-line", 1))
    )


_NndsxT1E1IfStatusTransmitClock_Type.__name__ = "Integer32"
_NndsxT1E1IfStatusTransmitClock_Object = MibTableColumn
nndsxT1E1IfStatusTransmitClock = _NndsxT1E1IfStatusTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2),
    _NndsxT1E1IfStatusTransmitClock_Type()
)
nndsxT1E1IfStatusTransmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfStatusTransmitClock.setStatus("current")
_NndsxT1E1IfAlarmStatusTable_Object = MibTable
nndsxT1E1IfAlarmStatusTable = _NndsxT1E1IfAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmStatusTable.setStatus("current")
_NndsxT1E1IfAlarmStatusEntry_Object = MibTableRow
nndsxT1E1IfAlarmStatusEntry = _NndsxT1E1IfAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmStatusEntry.setStatus("current")


class _NndsxT1E1IfAlarmStatusAlarmStatus_Type(Bits):
    """Custom type nndsxT1E1IfAlarmStatusAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("ibTestAlarm", 16),
          ("loopbackStateAlarm", 6),
          ("lorcAlarm", 13),
          ("raisAlarm", 2),
          ("rcpeAlarm", 12),
          ("rcvTestCode", 7),
          ("rexzAlarm", 9),
          ("rfebeAlarm", 10),
          ("risAlarm", 8),
          ("rlofAlarm", 4),
          ("rlosAlarm", 5),
          ("rpeAlarm", 11),
          ("rraiAlarm", 0),
          ("taisAlarm", 3),
          ("tfebeAlarm", 15),
          ("tpdeAlarm", 14),
          ("traiAlarm", 1))
    )

_NndsxT1E1IfAlarmStatusAlarmStatus_Type.__name__ = "Bits"
_NndsxT1E1IfAlarmStatusAlarmStatus_Object = MibTableColumn
nndsxT1E1IfAlarmStatusAlarmStatus = _NndsxT1E1IfAlarmStatusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1),
    _NndsxT1E1IfAlarmStatusAlarmStatus_Type()
)
nndsxT1E1IfAlarmStatusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmStatusAlarmStatus.setStatus("current")


class _NndsxT1E1IfAlarmStatusThresholdStatus_Type(Bits):
    """Custom type nndsxT1E1IfAlarmStatusThresholdStatus based on Bits"""
    namedValues = NamedValues(
        *(("threshold1", 0),
          ("threshold10", 9),
          ("threshold2", 1),
          ("threshold3", 2),
          ("threshold4", 3),
          ("threshold5", 4),
          ("threshold6", 5),
          ("threshold7", 6),
          ("threshold8", 7),
          ("threshold9", 8))
    )

_NndsxT1E1IfAlarmStatusThresholdStatus_Type.__name__ = "Bits"
_NndsxT1E1IfAlarmStatusThresholdStatus_Object = MibTableColumn
nndsxT1E1IfAlarmStatusThresholdStatus = _NndsxT1E1IfAlarmStatusThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2),
    _NndsxT1E1IfAlarmStatusThresholdStatus_Type()
)
nndsxT1E1IfAlarmStatusThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAlarmStatusThresholdStatus.setStatus("current")
_NndsxT1E1IfTestStatusTable_Object = MibTable
nndsxT1E1IfTestStatusTable = _NndsxT1E1IfTestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusTable.setStatus("current")
_NndsxT1E1IfTestStatusEntry_Object = MibTableRow
nndsxT1E1IfTestStatusEntry = _NndsxT1E1IfTestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusEntry.setStatus("current")


class _NndsxT1E1IfTestStatusTestType_Type(Integer32):
    """Custom type nndsxT1E1IfTestStatusTestType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("monitor-inject", 12),
          ("testtype-inward1-analog-loopback", 7),
          ("testtype-inward1-loopback", 6),
          ("testtype-inward2-loopback", 8),
          ("testtype-line-local-loopback", 5),
          ("testtype-line-loopback", 3),
          ("testtype-local-loopback", 4),
          ("testtype-notest", 1),
          ("testtype-pattern", 9),
          ("testtype-payload-loopback", 2),
          ("testtype-remote-lpdn", 11),
          ("testtype-remote-lpup", 10))
    )


_NndsxT1E1IfTestStatusTestType_Type.__name__ = "Integer32"
_NndsxT1E1IfTestStatusTestType_Object = MibTableColumn
nndsxT1E1IfTestStatusTestType = _NndsxT1E1IfTestStatusTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 1),
    _NndsxT1E1IfTestStatusTestType_Type()
)
nndsxT1E1IfTestStatusTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusTestType.setStatus("current")
_NndsxT1E1IfTestStatusTestTime_Type = Unsigned32
_NndsxT1E1IfTestStatusTestTime_Object = MibTableColumn
nndsxT1E1IfTestStatusTestTime = _NndsxT1E1IfTestStatusTestTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 2),
    _NndsxT1E1IfTestStatusTestTime_Type()
)
nndsxT1E1IfTestStatusTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusTestTime.setStatus("current")


class _NndsxT1E1IfTestStatusTestState_Type(Integer32):
    """Custom type nndsxT1E1IfTestStatusTestState based on Integer32"""
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
        *(("test-state-failed", 7),
          ("test-state-idle", 1),
          ("test-state-inprogress", 5),
          ("test-state-locked", 3),
          ("test-state-passed", 6),
          ("test-state-relocked", 4),
          ("test-state-searching", 2))
    )


_NndsxT1E1IfTestStatusTestState_Type.__name__ = "Integer32"
_NndsxT1E1IfTestStatusTestState_Object = MibTableColumn
nndsxT1E1IfTestStatusTestState = _NndsxT1E1IfTestStatusTestState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 3),
    _NndsxT1E1IfTestStatusTestState_Type()
)
nndsxT1E1IfTestStatusTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusTestState.setStatus("current")


class _NndsxT1E1IfTestStatusTestPattern_Type(Integer32):
    """Custom type nndsxT1E1IfTestStatusTestPattern based on Integer32"""
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
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("pattern-1in3", 5),
          ("pattern-1in5", 6),
          ("pattern-1in7", 7),
          ("pattern-211minus1", 21),
          ("pattern-215minus1", 13),
          ("pattern-220minus1", 14),
          ("pattern-223minus1", 16),
          ("pattern-29minus1", 12),
          ("pattern-3in24", 4),
          ("pattern-all-ones", 1),
          ("pattern-all-zeros", 2),
          ("pattern-alt-resetcod", 20),
          ("pattern-alt-setcode", 19),
          ("pattern-alternating", 3),
          ("pattern-none", 0),
          ("pattern-qrw", 15),
          ("pattern-smartjack-lpdown", 9),
          ("pattern-smartjack-lpup", 8),
          ("pattern-std-resetcod", 18),
          ("pattern-std-setcode", 17),
          ("pattern-user1", 10),
          ("pattern-user2", 11))
    )


_NndsxT1E1IfTestStatusTestPattern_Type.__name__ = "Integer32"
_NndsxT1E1IfTestStatusTestPattern_Object = MibTableColumn
nndsxT1E1IfTestStatusTestPattern = _NndsxT1E1IfTestStatusTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 4),
    _NndsxT1E1IfTestStatusTestPattern_Type()
)
nndsxT1E1IfTestStatusTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusTestPattern.setStatus("current")
_NndsxT1E1IfTestStatusLockedSeconds_Type = Unsigned32
_NndsxT1E1IfTestStatusLockedSeconds_Object = MibTableColumn
nndsxT1E1IfTestStatusLockedSeconds = _NndsxT1E1IfTestStatusLockedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 5),
    _NndsxT1E1IfTestStatusLockedSeconds_Type()
)
nndsxT1E1IfTestStatusLockedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusLockedSeconds.setStatus("current")
_NndsxT1E1IfTestStatusSyncLossCount_Type = Unsigned32
_NndsxT1E1IfTestStatusSyncLossCount_Object = MibTableColumn
nndsxT1E1IfTestStatusSyncLossCount = _NndsxT1E1IfTestStatusSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 6),
    _NndsxT1E1IfTestStatusSyncLossCount_Type()
)
nndsxT1E1IfTestStatusSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusSyncLossCount.setStatus("current")
_NndsxT1E1IfTestStatusErrorCount_Type = Unsigned32
_NndsxT1E1IfTestStatusErrorCount_Object = MibTableColumn
nndsxT1E1IfTestStatusErrorCount = _NndsxT1E1IfTestStatusErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 7),
    _NndsxT1E1IfTestStatusErrorCount_Type()
)
nndsxT1E1IfTestStatusErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusErrorCount.setStatus("current")


class _NndsxT1E1IfTestStatusLoopCode_Type(Integer32):
    """Custom type nndsxT1E1IfTestStatusLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("loopcode-line-alternate", 3),
          ("loopcode-line-ansiFDL", 4),
          ("loopcode-line-standard", 2),
          ("loopcode-none", 1),
          ("loopcode-payload-ATTFDL", 6),
          ("loopcode-payload-ansiFDL", 7),
          ("loopcode-smartjack", 9),
          ("loopcode-v54", 8))
    )


_NndsxT1E1IfTestStatusLoopCode_Type.__name__ = "Integer32"
_NndsxT1E1IfTestStatusLoopCode_Object = MibTableColumn
nndsxT1E1IfTestStatusLoopCode = _NndsxT1E1IfTestStatusLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 3, 1, 8),
    _NndsxT1E1IfTestStatusLoopCode_Type()
)
nndsxT1E1IfTestStatusLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfTestStatusLoopCode.setStatus("current")
_NndsxT1E1IfLastTestResultTable_Object = MibTable
nndsxT1E1IfLastTestResultTable = _NndsxT1E1IfLastTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultTable.setStatus("current")
_NndsxT1E1IfLastTestResultEntry_Object = MibTableRow
nndsxT1E1IfLastTestResultEntry = _NndsxT1E1IfLastTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultEntry.setStatus("current")


class _NndsxT1E1IfLastTestResultTestType_Type(Integer32):
    """Custom type nndsxT1E1IfLastTestResultTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("testtype-line-loopback", 3),
          ("testtype-notest", 1),
          ("testtype-pattern", 9),
          ("testtype-payload-loopback", 2),
          ("testtype-remote-lpdn", 11),
          ("testtype-remote-lpup", 10))
    )


_NndsxT1E1IfLastTestResultTestType_Type.__name__ = "Integer32"
_NndsxT1E1IfLastTestResultTestType_Object = MibTableColumn
nndsxT1E1IfLastTestResultTestType = _NndsxT1E1IfLastTestResultTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 1),
    _NndsxT1E1IfLastTestResultTestType_Type()
)
nndsxT1E1IfLastTestResultTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultTestType.setStatus("current")
_NndsxT1E1IfLastTestResultTestTime_Type = Unsigned32
_NndsxT1E1IfLastTestResultTestTime_Object = MibTableColumn
nndsxT1E1IfLastTestResultTestTime = _NndsxT1E1IfLastTestResultTestTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 2),
    _NndsxT1E1IfLastTestResultTestTime_Type()
)
nndsxT1E1IfLastTestResultTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultTestTime.setStatus("current")


class _NndsxT1E1IfLastTestResultTestState_Type(Integer32):
    """Custom type nndsxT1E1IfLastTestResultTestState based on Integer32"""
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
        *(("test-state-failed", 7),
          ("test-state-idle", 1),
          ("test-state-inprogress", 5),
          ("test-state-locked", 3),
          ("test-state-passed", 6),
          ("test-state-relocked", 4),
          ("test-state-searching", 2))
    )


_NndsxT1E1IfLastTestResultTestState_Type.__name__ = "Integer32"
_NndsxT1E1IfLastTestResultTestState_Object = MibTableColumn
nndsxT1E1IfLastTestResultTestState = _NndsxT1E1IfLastTestResultTestState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 3),
    _NndsxT1E1IfLastTestResultTestState_Type()
)
nndsxT1E1IfLastTestResultTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultTestState.setStatus("current")


class _NndsxT1E1IfLastTestResultTestPattern_Type(Integer32):
    """Custom type nndsxT1E1IfLastTestResultTestPattern based on Integer32"""
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
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("pattern-1in3", 5),
          ("pattern-1in5", 6),
          ("pattern-1in7", 7),
          ("pattern-211minus1", 21),
          ("pattern-215minus1", 13),
          ("pattern-220minus1", 14),
          ("pattern-223minus1", 16),
          ("pattern-29minus1", 12),
          ("pattern-3in24", 4),
          ("pattern-all-ones", 1),
          ("pattern-all-zeros", 2),
          ("pattern-alt-resetcod", 20),
          ("pattern-alt-setcode", 19),
          ("pattern-alternating", 3),
          ("pattern-none", 0),
          ("pattern-qrw", 15),
          ("pattern-smartjack-lpdown", 9),
          ("pattern-smartjack-lpup", 8),
          ("pattern-std-resetcod", 18),
          ("pattern-std-setcode", 17),
          ("pattern-user1", 10),
          ("pattern-user2", 11))
    )


_NndsxT1E1IfLastTestResultTestPattern_Type.__name__ = "Integer32"
_NndsxT1E1IfLastTestResultTestPattern_Object = MibTableColumn
nndsxT1E1IfLastTestResultTestPattern = _NndsxT1E1IfLastTestResultTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 4),
    _NndsxT1E1IfLastTestResultTestPattern_Type()
)
nndsxT1E1IfLastTestResultTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultTestPattern.setStatus("current")
_NndsxT1E1IfLastTestResultLockedSeconds_Type = Unsigned32
_NndsxT1E1IfLastTestResultLockedSeconds_Object = MibTableColumn
nndsxT1E1IfLastTestResultLockedSeconds = _NndsxT1E1IfLastTestResultLockedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 5),
    _NndsxT1E1IfLastTestResultLockedSeconds_Type()
)
nndsxT1E1IfLastTestResultLockedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultLockedSeconds.setStatus("current")
_NndsxT1E1IfLastTestResultSyncLossCount_Type = Unsigned32
_NndsxT1E1IfLastTestResultSyncLossCount_Object = MibTableColumn
nndsxT1E1IfLastTestResultSyncLossCount = _NndsxT1E1IfLastTestResultSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 6),
    _NndsxT1E1IfLastTestResultSyncLossCount_Type()
)
nndsxT1E1IfLastTestResultSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultSyncLossCount.setStatus("current")
_NndsxT1E1IfLastTestResultErrorCount_Type = Unsigned32
_NndsxT1E1IfLastTestResultErrorCount_Object = MibTableColumn
nndsxT1E1IfLastTestResultErrorCount = _NndsxT1E1IfLastTestResultErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 7),
    _NndsxT1E1IfLastTestResultErrorCount_Type()
)
nndsxT1E1IfLastTestResultErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultErrorCount.setStatus("current")


class _NndsxT1E1IfLastTestResultLoopCode_Type(Integer32):
    """Custom type nndsxT1E1IfLastTestResultLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("loopcode-line-alternate", 3),
          ("loopcode-line-ansiFDL", 4),
          ("loopcode-line-standard", 2),
          ("loopcode-none", 1),
          ("loopcode-payload-ATTFDL", 6),
          ("loopcode-payload-ansiFDL", 7),
          ("loopcode-smartjack", 9),
          ("loopcode-v54", 8))
    )


_NndsxT1E1IfLastTestResultLoopCode_Type.__name__ = "Integer32"
_NndsxT1E1IfLastTestResultLoopCode_Object = MibTableColumn
nndsxT1E1IfLastTestResultLoopCode = _NndsxT1E1IfLastTestResultLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 2, 4, 1, 8),
    _NndsxT1E1IfLastTestResultLoopCode_Type()
)
nndsxT1E1IfLastTestResultLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfLastTestResultLoopCode.setStatus("current")
_NndsxT1E1IfStatsGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfStatsGroup = _NndsxT1E1IfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3)
)
_NndsxT1E1IfArchiveStatsValidIntervalsTable_Object = MibTable
nndsxT1E1IfArchiveStatsValidIntervalsTable = _NndsxT1E1IfArchiveStatsValidIntervalsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfArchiveStatsValidIntervalsTable.setStatus("current")
_NndsxT1E1IfArchiveStatsValidIntervalsEntry_Object = MibTableRow
nndsxT1E1IfArchiveStatsValidIntervalsEntry = _NndsxT1E1IfArchiveStatsValidIntervalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfArchiveStatsValidIntervalsEntry.setStatus("current")
_NndsxT1E1IfAnsiArchiveStatsValidIntervals_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveStatsValidIntervals_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveStatsValidIntervals = _NndsxT1E1IfAnsiArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1, 1),
    _NndsxT1E1IfAnsiArchiveStatsValidIntervals_Type()
)
nndsxT1E1IfAnsiArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveStatsValidIntervals.setStatus("current")
_NndsxT1E1IfAttArchiveStatsValidIntervals_Type = Unsigned32
_NndsxT1E1IfAttArchiveStatsValidIntervals_Object = MibTableColumn
nndsxT1E1IfAttArchiveStatsValidIntervals = _NndsxT1E1IfAttArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1, 2),
    _NndsxT1E1IfAttArchiveStatsValidIntervals_Type()
)
nndsxT1E1IfAttArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsValidIntervals.setStatus("current")
_NndsxT1E1IfItutArchiveStatsValidIntervals_Type = Unsigned32
_NndsxT1E1IfItutArchiveStatsValidIntervals_Object = MibTableColumn
nndsxT1E1IfItutArchiveStatsValidIntervals = _NndsxT1E1IfItutArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1, 3),
    _NndsxT1E1IfItutArchiveStatsValidIntervals_Type()
)
nndsxT1E1IfItutArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsValidIntervals.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsValidIntervals_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsValidIntervals_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsValidIntervals = _NndsxT1E1IfIetfArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1, 4),
    _NndsxT1E1IfIetfArchiveStatsValidIntervals_Type()
)
nndsxT1E1IfIetfArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsValidIntervals.setStatus("current")
_NndsxT1E1IfUserTotalStatsValidDays_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsValidDays_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsValidDays = _NndsxT1E1IfUserTotalStatsValidDays_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1, 5),
    _NndsxT1E1IfUserTotalStatsValidDays_Type()
)
nndsxT1E1IfUserTotalStatsValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsValidDays.setStatus("current")
_NndsxT1E1IfUserArchiveStatsValidIntervals_Type = Integer32
_NndsxT1E1IfUserArchiveStatsValidIntervals_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsValidIntervals = _NndsxT1E1IfUserArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 1, 1, 6),
    _NndsxT1E1IfUserArchiveStatsValidIntervals_Type()
)
nndsxT1E1IfUserArchiveStatsValidIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsValidIntervals.setStatus("current")
_NndsxT1E1IfAnsiStatsGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfAnsiStatsGroup = _NndsxT1E1IfAnsiStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2)
)
_NndsxT1E1IfAnsiCurrentStatsTable_Object = MibTable
nndsxT1E1IfAnsiCurrentStatsTable = _NndsxT1E1IfAnsiCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentStatsTable.setStatus("current")
_NndsxT1E1IfAnsiCurrentStatsEntry_Object = MibTableRow
nndsxT1E1IfAnsiCurrentStatsEntry = _NndsxT1E1IfAnsiCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentStatsEntry.setStatus("current")
_NndsxT1E1IfAnsiCurrentStatsUASState_Type = TruthValue
_NndsxT1E1IfAnsiCurrentStatsUASState_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentStatsUASState = _NndsxT1E1IfAnsiCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 1),
    _NndsxT1E1IfAnsiCurrentStatsUASState_Type()
)
nndsxT1E1IfAnsiCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentStatsUASState.setStatus("current")
_NndsxT1E1IfAnsiCurrentStatsTimeInCurrent_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentStatsTimeInCurrent_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentStatsTimeInCurrent = _NndsxT1E1IfAnsiCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 2),
    _NndsxT1E1IfAnsiCurrentStatsTimeInCurrent_Type()
)
nndsxT1E1IfAnsiCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentStatsTimeInCurrent.setStatus("current")
_NndsxT1E1IfAnsiCurrentPathStatsCV_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentPathStatsCV_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentPathStatsCV = _NndsxT1E1IfAnsiCurrentPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 3),
    _NndsxT1E1IfAnsiCurrentPathStatsCV_Type()
)
nndsxT1E1IfAnsiCurrentPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentPathStatsCV.setStatus("current")
_NndsxT1E1IfAnsiCurrentPathStatsES_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentPathStatsES_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentPathStatsES = _NndsxT1E1IfAnsiCurrentPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 4),
    _NndsxT1E1IfAnsiCurrentPathStatsES_Type()
)
nndsxT1E1IfAnsiCurrentPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentPathStatsES.setStatus("current")
_NndsxT1E1IfAnsiCurrentPathStatsSES_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentPathStatsSES_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentPathStatsSES = _NndsxT1E1IfAnsiCurrentPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 5),
    _NndsxT1E1IfAnsiCurrentPathStatsSES_Type()
)
nndsxT1E1IfAnsiCurrentPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentPathStatsSES.setStatus("current")
_NndsxT1E1IfAnsiCurrentPathStatsSAS_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentPathStatsSAS_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentPathStatsSAS = _NndsxT1E1IfAnsiCurrentPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 6),
    _NndsxT1E1IfAnsiCurrentPathStatsSAS_Type()
)
nndsxT1E1IfAnsiCurrentPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentPathStatsSAS.setStatus("current")
_NndsxT1E1IfAnsiCurrentPathStatsCSS_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentPathStatsCSS_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentPathStatsCSS = _NndsxT1E1IfAnsiCurrentPathStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 7),
    _NndsxT1E1IfAnsiCurrentPathStatsCSS_Type()
)
nndsxT1E1IfAnsiCurrentPathStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentPathStatsCSS.setStatus("current")
_NndsxT1E1IfAnsiCurrentPathStatsUAS_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentPathStatsUAS_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentPathStatsUAS = _NndsxT1E1IfAnsiCurrentPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 8),
    _NndsxT1E1IfAnsiCurrentPathStatsUAS_Type()
)
nndsxT1E1IfAnsiCurrentPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentPathStatsUAS.setStatus("current")
_NndsxT1E1IfAnsiCurrentLineStatsCV_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentLineStatsCV_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentLineStatsCV = _NndsxT1E1IfAnsiCurrentLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 9),
    _NndsxT1E1IfAnsiCurrentLineStatsCV_Type()
)
nndsxT1E1IfAnsiCurrentLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentLineStatsCV.setStatus("current")
_NndsxT1E1IfAnsiCurrentLineStatsES_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentLineStatsES_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentLineStatsES = _NndsxT1E1IfAnsiCurrentLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 10),
    _NndsxT1E1IfAnsiCurrentLineStatsES_Type()
)
nndsxT1E1IfAnsiCurrentLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentLineStatsES.setStatus("current")
_NndsxT1E1IfAnsiCurrentLineStatsSES_Type = Unsigned32
_NndsxT1E1IfAnsiCurrentLineStatsSES_Object = MibTableColumn
nndsxT1E1IfAnsiCurrentLineStatsSES = _NndsxT1E1IfAnsiCurrentLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 1, 1, 11),
    _NndsxT1E1IfAnsiCurrentLineStatsSES_Type()
)
nndsxT1E1IfAnsiCurrentLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiCurrentLineStatsSES.setStatus("current")
_NndsxT1E1IfAnsiTotalStatsTable_Object = MibTable
nndsxT1E1IfAnsiTotalStatsTable = _NndsxT1E1IfAnsiTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalStatsTable.setStatus("current")
_NndsxT1E1IfAnsiTotalStatsEntry_Object = MibTableRow
nndsxT1E1IfAnsiTotalStatsEntry = _NndsxT1E1IfAnsiTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalStatsEntry.setStatus("current")
_NndsxT1E1IfAnsiTotalPathStatsCV_Type = Unsigned32
_NndsxT1E1IfAnsiTotalPathStatsCV_Object = MibTableColumn
nndsxT1E1IfAnsiTotalPathStatsCV = _NndsxT1E1IfAnsiTotalPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 1),
    _NndsxT1E1IfAnsiTotalPathStatsCV_Type()
)
nndsxT1E1IfAnsiTotalPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalPathStatsCV.setStatus("current")
_NndsxT1E1IfAnsiTotalPathStatsES_Type = Unsigned32
_NndsxT1E1IfAnsiTotalPathStatsES_Object = MibTableColumn
nndsxT1E1IfAnsiTotalPathStatsES = _NndsxT1E1IfAnsiTotalPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 2),
    _NndsxT1E1IfAnsiTotalPathStatsES_Type()
)
nndsxT1E1IfAnsiTotalPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalPathStatsES.setStatus("current")
_NndsxT1E1IfAnsiTotalPathStatsSES_Type = Unsigned32
_NndsxT1E1IfAnsiTotalPathStatsSES_Object = MibTableColumn
nndsxT1E1IfAnsiTotalPathStatsSES = _NndsxT1E1IfAnsiTotalPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3),
    _NndsxT1E1IfAnsiTotalPathStatsSES_Type()
)
nndsxT1E1IfAnsiTotalPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalPathStatsSES.setStatus("current")
_NndsxT1E1IfAnsiTotalPathStatsSAS_Type = Unsigned32
_NndsxT1E1IfAnsiTotalPathStatsSAS_Object = MibTableColumn
nndsxT1E1IfAnsiTotalPathStatsSAS = _NndsxT1E1IfAnsiTotalPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4),
    _NndsxT1E1IfAnsiTotalPathStatsSAS_Type()
)
nndsxT1E1IfAnsiTotalPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalPathStatsSAS.setStatus("current")
_NndsxT1E1IfAnsiTotalPathStatsCSS_Type = Unsigned32
_NndsxT1E1IfAnsiTotalPathStatsCSS_Object = MibTableColumn
nndsxT1E1IfAnsiTotalPathStatsCSS = _NndsxT1E1IfAnsiTotalPathStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 5),
    _NndsxT1E1IfAnsiTotalPathStatsCSS_Type()
)
nndsxT1E1IfAnsiTotalPathStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalPathStatsCSS.setStatus("current")
_NndsxT1E1IfAnsiTotalPathStatsUAS_Type = Unsigned32
_NndsxT1E1IfAnsiTotalPathStatsUAS_Object = MibTableColumn
nndsxT1E1IfAnsiTotalPathStatsUAS = _NndsxT1E1IfAnsiTotalPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 6),
    _NndsxT1E1IfAnsiTotalPathStatsUAS_Type()
)
nndsxT1E1IfAnsiTotalPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalPathStatsUAS.setStatus("current")
_NndsxT1E1IfAnsiTotalLineStatsCV_Type = Unsigned32
_NndsxT1E1IfAnsiTotalLineStatsCV_Object = MibTableColumn
nndsxT1E1IfAnsiTotalLineStatsCV = _NndsxT1E1IfAnsiTotalLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 7),
    _NndsxT1E1IfAnsiTotalLineStatsCV_Type()
)
nndsxT1E1IfAnsiTotalLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalLineStatsCV.setStatus("current")
_NndsxT1E1IfAnsiTotalLineStatsES_Type = Unsigned32
_NndsxT1E1IfAnsiTotalLineStatsES_Object = MibTableColumn
nndsxT1E1IfAnsiTotalLineStatsES = _NndsxT1E1IfAnsiTotalLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 8),
    _NndsxT1E1IfAnsiTotalLineStatsES_Type()
)
nndsxT1E1IfAnsiTotalLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalLineStatsES.setStatus("current")
_NndsxT1E1IfAnsiTotalLineStatsSES_Type = Unsigned32
_NndsxT1E1IfAnsiTotalLineStatsSES_Object = MibTableColumn
nndsxT1E1IfAnsiTotalLineStatsSES = _NndsxT1E1IfAnsiTotalLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 9),
    _NndsxT1E1IfAnsiTotalLineStatsSES_Type()
)
nndsxT1E1IfAnsiTotalLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiTotalLineStatsSES.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalStatsTable_Object = MibTable
nndsxT1E1IfAnsiArchiveIntervalStatsTable = _NndsxT1E1IfAnsiArchiveIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalStatsTable.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalStatsEntry_Object = MibTableRow
nndsxT1E1IfAnsiArchiveIntervalStatsEntry = _NndsxT1E1IfAnsiArchiveIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1)
)
nndsxT1E1IfAnsiArchiveIntervalStatsEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfAnsiArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalStatsEntry.setStatus("current")
_NndsxT1E1IfAnsiArchiveStatsInterval_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveStatsInterval_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveStatsInterval = _NndsxT1E1IfAnsiArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 1),
    _NndsxT1E1IfAnsiArchiveStatsInterval_Type()
)
nndsxT1E1IfAnsiArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveStatsInterval.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalPathStatsCV_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalPathStatsCV_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalPathStatsCV = _NndsxT1E1IfAnsiArchiveIntervalPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 2),
    _NndsxT1E1IfAnsiArchiveIntervalPathStatsCV_Type()
)
nndsxT1E1IfAnsiArchiveIntervalPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalPathStatsCV.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalPathStatsES_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalPathStatsES_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalPathStatsES = _NndsxT1E1IfAnsiArchiveIntervalPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 3),
    _NndsxT1E1IfAnsiArchiveIntervalPathStatsES_Type()
)
nndsxT1E1IfAnsiArchiveIntervalPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalPathStatsES.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalPathStatsSES_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalPathStatsSES_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalPathStatsSES = _NndsxT1E1IfAnsiArchiveIntervalPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 4),
    _NndsxT1E1IfAnsiArchiveIntervalPathStatsSES_Type()
)
nndsxT1E1IfAnsiArchiveIntervalPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalPathStatsSES.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalPathStatsSAS = _NndsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 5),
    _NndsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Type()
)
nndsxT1E1IfAnsiArchiveIntervalPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalPathStatsSAS.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalPathStatsCSS = _NndsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 6),
    _NndsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Type()
)
nndsxT1E1IfAnsiArchiveIntervalPathStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalPathStatsCSS.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalPathStatsUAS = _NndsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 7),
    _NndsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Type()
)
nndsxT1E1IfAnsiArchiveIntervalPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalPathStatsUAS.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalLineStatsCV_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalLineStatsCV_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalLineStatsCV = _NndsxT1E1IfAnsiArchiveIntervalLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 8),
    _NndsxT1E1IfAnsiArchiveIntervalLineStatsCV_Type()
)
nndsxT1E1IfAnsiArchiveIntervalLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalLineStatsCV.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalLineStatsES_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalLineStatsES_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalLineStatsES = _NndsxT1E1IfAnsiArchiveIntervalLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 9),
    _NndsxT1E1IfAnsiArchiveIntervalLineStatsES_Type()
)
nndsxT1E1IfAnsiArchiveIntervalLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalLineStatsES.setStatus("current")
_NndsxT1E1IfAnsiArchiveIntervalLineStatsSES_Type = Unsigned32
_NndsxT1E1IfAnsiArchiveIntervalLineStatsSES_Object = MibTableColumn
nndsxT1E1IfAnsiArchiveIntervalLineStatsSES = _NndsxT1E1IfAnsiArchiveIntervalLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 10),
    _NndsxT1E1IfAnsiArchiveIntervalLineStatsSES_Type()
)
nndsxT1E1IfAnsiArchiveIntervalLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAnsiArchiveIntervalLineStatsSES.setStatus("current")
_NndsxT1E1IfAttStatsGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfAttStatsGroup = _NndsxT1E1IfAttStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3)
)
_NndsxT1E1IfAttCurrentStatsTable_Object = MibTable
nndsxT1E1IfAttCurrentStatsTable = _NndsxT1E1IfAttCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsTable.setStatus("current")
_NndsxT1E1IfAttCurrentStatsEntry_Object = MibTableRow
nndsxT1E1IfAttCurrentStatsEntry = _NndsxT1E1IfAttCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsEntry.setStatus("current")
_NndsxT1E1IfAttCurrentStatsUASState_Type = TruthValue
_NndsxT1E1IfAttCurrentStatsUASState_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsUASState = _NndsxT1E1IfAttCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 1),
    _NndsxT1E1IfAttCurrentStatsUASState_Type()
)
nndsxT1E1IfAttCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsUASState.setStatus("current")
_NndsxT1E1IfAttCurrentStatsTimeInCurrent_Type = Unsigned32
_NndsxT1E1IfAttCurrentStatsTimeInCurrent_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsTimeInCurrent = _NndsxT1E1IfAttCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 2),
    _NndsxT1E1IfAttCurrentStatsTimeInCurrent_Type()
)
nndsxT1E1IfAttCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsTimeInCurrent.setStatus("current")
_NndsxT1E1IfAttCurrentStatsEEV_Type = Unsigned32
_NndsxT1E1IfAttCurrentStatsEEV_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsEEV = _NndsxT1E1IfAttCurrentStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 3),
    _NndsxT1E1IfAttCurrentStatsEEV_Type()
)
nndsxT1E1IfAttCurrentStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsEEV.setStatus("current")
_NndsxT1E1IfAttCurrentStatsES_Type = Unsigned32
_NndsxT1E1IfAttCurrentStatsES_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsES = _NndsxT1E1IfAttCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 4),
    _NndsxT1E1IfAttCurrentStatsES_Type()
)
nndsxT1E1IfAttCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsES.setStatus("current")
_NndsxT1E1IfAttCurrentStatsUAS_Type = Unsigned32
_NndsxT1E1IfAttCurrentStatsUAS_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsUAS = _NndsxT1E1IfAttCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 5),
    _NndsxT1E1IfAttCurrentStatsUAS_Type()
)
nndsxT1E1IfAttCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsUAS.setStatus("current")
_NndsxT1E1IfAttCurrentStatsSES_Type = Unsigned32
_NndsxT1E1IfAttCurrentStatsSES_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsSES = _NndsxT1E1IfAttCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 7),
    _NndsxT1E1IfAttCurrentStatsSES_Type()
)
nndsxT1E1IfAttCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsSES.setStatus("current")
_NndsxT1E1IfAttCurrentStatsCSS_Type = Unsigned32
_NndsxT1E1IfAttCurrentStatsCSS_Object = MibTableColumn
nndsxT1E1IfAttCurrentStatsCSS = _NndsxT1E1IfAttCurrentStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 1, 1, 9),
    _NndsxT1E1IfAttCurrentStatsCSS_Type()
)
nndsxT1E1IfAttCurrentStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttCurrentStatsCSS.setStatus("current")
_NndsxT1E1IfAttTotalStatsTable_Object = MibTable
nndsxT1E1IfAttTotalStatsTable = _NndsxT1E1IfAttTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsTable.setStatus("current")
_NndsxT1E1IfAttTotalStatsEntry_Object = MibTableRow
nndsxT1E1IfAttTotalStatsEntry = _NndsxT1E1IfAttTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsEntry.setStatus("current")
_NndsxT1E1IfAttTotalStatsEEV_Type = Unsigned32
_NndsxT1E1IfAttTotalStatsEEV_Object = MibTableColumn
nndsxT1E1IfAttTotalStatsEEV = _NndsxT1E1IfAttTotalStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2, 1, 1),
    _NndsxT1E1IfAttTotalStatsEEV_Type()
)
nndsxT1E1IfAttTotalStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsEEV.setStatus("current")
_NndsxT1E1IfAttTotalStatsES_Type = Unsigned32
_NndsxT1E1IfAttTotalStatsES_Object = MibTableColumn
nndsxT1E1IfAttTotalStatsES = _NndsxT1E1IfAttTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2, 1, 2),
    _NndsxT1E1IfAttTotalStatsES_Type()
)
nndsxT1E1IfAttTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsES.setStatus("current")
_NndsxT1E1IfAttTotalStatsUAS_Type = Unsigned32
_NndsxT1E1IfAttTotalStatsUAS_Object = MibTableColumn
nndsxT1E1IfAttTotalStatsUAS = _NndsxT1E1IfAttTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2, 1, 3),
    _NndsxT1E1IfAttTotalStatsUAS_Type()
)
nndsxT1E1IfAttTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsUAS.setStatus("current")
_NndsxT1E1IfAttTotalStatsSES_Type = Unsigned32
_NndsxT1E1IfAttTotalStatsSES_Object = MibTableColumn
nndsxT1E1IfAttTotalStatsSES = _NndsxT1E1IfAttTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2, 1, 5),
    _NndsxT1E1IfAttTotalStatsSES_Type()
)
nndsxT1E1IfAttTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsSES.setStatus("current")
_NndsxT1E1IfAttTotalStatsCSS_Type = Unsigned32
_NndsxT1E1IfAttTotalStatsCSS_Object = MibTableColumn
nndsxT1E1IfAttTotalStatsCSS = _NndsxT1E1IfAttTotalStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 2, 1, 7),
    _NndsxT1E1IfAttTotalStatsCSS_Type()
)
nndsxT1E1IfAttTotalStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttTotalStatsCSS.setStatus("current")
_NndsxT1E1IfAttArchiveStatsTable_Object = MibTable
nndsxT1E1IfAttArchiveStatsTable = _NndsxT1E1IfAttArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsTable.setStatus("current")
_NndsxT1E1IfAttArchiveStatsEntry_Object = MibTableRow
nndsxT1E1IfAttArchiveStatsEntry = _NndsxT1E1IfAttArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1)
)
nndsxT1E1IfAttArchiveStatsEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfAttArchiveInterval"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsEntry.setStatus("current")
_NndsxT1E1IfAttArchiveInterval_Type = Unsigned32
_NndsxT1E1IfAttArchiveInterval_Object = MibTableColumn
nndsxT1E1IfAttArchiveInterval = _NndsxT1E1IfAttArchiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1, 1),
    _NndsxT1E1IfAttArchiveInterval_Type()
)
nndsxT1E1IfAttArchiveInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveInterval.setStatus("current")
_NndsxT1E1IfAttArchiveStatsEEV_Type = Unsigned32
_NndsxT1E1IfAttArchiveStatsEEV_Object = MibTableColumn
nndsxT1E1IfAttArchiveStatsEEV = _NndsxT1E1IfAttArchiveStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1, 2),
    _NndsxT1E1IfAttArchiveStatsEEV_Type()
)
nndsxT1E1IfAttArchiveStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsEEV.setStatus("current")
_NndsxT1E1IfAttArchiveStatsES_Type = Unsigned32
_NndsxT1E1IfAttArchiveStatsES_Object = MibTableColumn
nndsxT1E1IfAttArchiveStatsES = _NndsxT1E1IfAttArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1, 3),
    _NndsxT1E1IfAttArchiveStatsES_Type()
)
nndsxT1E1IfAttArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsES.setStatus("current")
_NndsxT1E1IfAttArchiveStatsUAS_Type = Unsigned32
_NndsxT1E1IfAttArchiveStatsUAS_Object = MibTableColumn
nndsxT1E1IfAttArchiveStatsUAS = _NndsxT1E1IfAttArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1, 4),
    _NndsxT1E1IfAttArchiveStatsUAS_Type()
)
nndsxT1E1IfAttArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsUAS.setStatus("current")
_NndsxT1E1IfAttArchiveStatsSES_Type = Unsigned32
_NndsxT1E1IfAttArchiveStatsSES_Object = MibTableColumn
nndsxT1E1IfAttArchiveStatsSES = _NndsxT1E1IfAttArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1, 6),
    _NndsxT1E1IfAttArchiveStatsSES_Type()
)
nndsxT1E1IfAttArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsSES.setStatus("current")
_NndsxT1E1IfAttArchiveStatsCSS_Type = Unsigned32
_NndsxT1E1IfAttArchiveStatsCSS_Object = MibTableColumn
nndsxT1E1IfAttArchiveStatsCSS = _NndsxT1E1IfAttArchiveStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 3, 3, 1, 8),
    _NndsxT1E1IfAttArchiveStatsCSS_Type()
)
nndsxT1E1IfAttArchiveStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfAttArchiveStatsCSS.setStatus("current")
_NndsxT1E1IfItutStatsGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfItutStatsGroup = _NndsxT1E1IfItutStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4)
)
_NndsxT1E1IfItutCurrentStatsTable_Object = MibTable
nndsxT1E1IfItutCurrentStatsTable = _NndsxT1E1IfItutCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsTable.setStatus("current")
_NndsxT1E1IfItutCurrentStatsEntry_Object = MibTableRow
nndsxT1E1IfItutCurrentStatsEntry = _NndsxT1E1IfItutCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsEntry.setStatus("current")
_NndsxT1E1IfItutCurrentStatsUASState_Type = TruthValue
_NndsxT1E1IfItutCurrentStatsUASState_Object = MibTableColumn
nndsxT1E1IfItutCurrentStatsUASState = _NndsxT1E1IfItutCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1, 1),
    _NndsxT1E1IfItutCurrentStatsUASState_Type()
)
nndsxT1E1IfItutCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsUASState.setStatus("current")
_NndsxT1E1IfItutCurrentStatsTimeInCurrent_Type = Unsigned32
_NndsxT1E1IfItutCurrentStatsTimeInCurrent_Object = MibTableColumn
nndsxT1E1IfItutCurrentStatsTimeInCurrent = _NndsxT1E1IfItutCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1, 2),
    _NndsxT1E1IfItutCurrentStatsTimeInCurrent_Type()
)
nndsxT1E1IfItutCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsTimeInCurrent.setStatus("current")
_NndsxT1E1IfItutCurrentStatsES_Type = Unsigned32
_NndsxT1E1IfItutCurrentStatsES_Object = MibTableColumn
nndsxT1E1IfItutCurrentStatsES = _NndsxT1E1IfItutCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1, 3),
    _NndsxT1E1IfItutCurrentStatsES_Type()
)
nndsxT1E1IfItutCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsES.setStatus("current")
_NndsxT1E1IfItutCurrentStatsUAS_Type = Unsigned32
_NndsxT1E1IfItutCurrentStatsUAS_Object = MibTableColumn
nndsxT1E1IfItutCurrentStatsUAS = _NndsxT1E1IfItutCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1, 4),
    _NndsxT1E1IfItutCurrentStatsUAS_Type()
)
nndsxT1E1IfItutCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsUAS.setStatus("current")
_NndsxT1E1IfItutCurrentStatsBBE_Type = Unsigned32
_NndsxT1E1IfItutCurrentStatsBBE_Object = MibTableColumn
nndsxT1E1IfItutCurrentStatsBBE = _NndsxT1E1IfItutCurrentStatsBBE_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1, 5),
    _NndsxT1E1IfItutCurrentStatsBBE_Type()
)
nndsxT1E1IfItutCurrentStatsBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsBBE.setStatus("current")
_NndsxT1E1IfItutCurrentStatsSES_Type = Unsigned32
_NndsxT1E1IfItutCurrentStatsSES_Object = MibTableColumn
nndsxT1E1IfItutCurrentStatsSES = _NndsxT1E1IfItutCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 1, 1, 6),
    _NndsxT1E1IfItutCurrentStatsSES_Type()
)
nndsxT1E1IfItutCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutCurrentStatsSES.setStatus("current")
_NndsxT1E1IfItutTotalStatsTable_Object = MibTable
nndsxT1E1IfItutTotalStatsTable = _NndsxT1E1IfItutTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfItutTotalStatsTable.setStatus("current")
_NndsxT1E1IfItutTotalStatsEntry_Object = MibTableRow
nndsxT1E1IfItutTotalStatsEntry = _NndsxT1E1IfItutTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfItutTotalStatsEntry.setStatus("current")
_NndsxT1E1IfItutTotalStatsES_Type = Unsigned32
_NndsxT1E1IfItutTotalStatsES_Object = MibTableColumn
nndsxT1E1IfItutTotalStatsES = _NndsxT1E1IfItutTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 2, 1, 1),
    _NndsxT1E1IfItutTotalStatsES_Type()
)
nndsxT1E1IfItutTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutTotalStatsES.setStatus("current")
_NndsxT1E1IfItutTotalStatsUAS_Type = Unsigned32
_NndsxT1E1IfItutTotalStatsUAS_Object = MibTableColumn
nndsxT1E1IfItutTotalStatsUAS = _NndsxT1E1IfItutTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 2, 1, 2),
    _NndsxT1E1IfItutTotalStatsUAS_Type()
)
nndsxT1E1IfItutTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutTotalStatsUAS.setStatus("current")
_NndsxT1E1IfItutTotalStatsBBE_Type = Unsigned32
_NndsxT1E1IfItutTotalStatsBBE_Object = MibTableColumn
nndsxT1E1IfItutTotalStatsBBE = _NndsxT1E1IfItutTotalStatsBBE_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 2, 1, 3),
    _NndsxT1E1IfItutTotalStatsBBE_Type()
)
nndsxT1E1IfItutTotalStatsBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutTotalStatsBBE.setStatus("current")
_NndsxT1E1IfItutTotalStatsSES_Type = Unsigned32
_NndsxT1E1IfItutTotalStatsSES_Object = MibTableColumn
nndsxT1E1IfItutTotalStatsSES = _NndsxT1E1IfItutTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 2, 1, 4),
    _NndsxT1E1IfItutTotalStatsSES_Type()
)
nndsxT1E1IfItutTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutTotalStatsSES.setStatus("current")
_NndsxT1E1IfItutArchiveStatsTable_Object = MibTable
nndsxT1E1IfItutArchiveStatsTable = _NndsxT1E1IfItutArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsTable.setStatus("current")
_NndsxT1E1IfItutArchiveStatsEntry_Object = MibTableRow
nndsxT1E1IfItutArchiveStatsEntry = _NndsxT1E1IfItutArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3, 1)
)
nndsxT1E1IfItutArchiveStatsEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfItutArchiveInterval"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsEntry.setStatus("current")
_NndsxT1E1IfItutArchiveInterval_Type = Unsigned32
_NndsxT1E1IfItutArchiveInterval_Object = MibTableColumn
nndsxT1E1IfItutArchiveInterval = _NndsxT1E1IfItutArchiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3, 1, 1),
    _NndsxT1E1IfItutArchiveInterval_Type()
)
nndsxT1E1IfItutArchiveInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveInterval.setStatus("current")
_NndsxT1E1IfItutArchiveStatsES_Type = Unsigned32
_NndsxT1E1IfItutArchiveStatsES_Object = MibTableColumn
nndsxT1E1IfItutArchiveStatsES = _NndsxT1E1IfItutArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3, 1, 2),
    _NndsxT1E1IfItutArchiveStatsES_Type()
)
nndsxT1E1IfItutArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsES.setStatus("current")
_NndsxT1E1IfItutArchiveStatsUAS_Type = Unsigned32
_NndsxT1E1IfItutArchiveStatsUAS_Object = MibTableColumn
nndsxT1E1IfItutArchiveStatsUAS = _NndsxT1E1IfItutArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3, 1, 3),
    _NndsxT1E1IfItutArchiveStatsUAS_Type()
)
nndsxT1E1IfItutArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsUAS.setStatus("current")
_NndsxT1E1IfItutArchiveStatsBBE_Type = Unsigned32
_NndsxT1E1IfItutArchiveStatsBBE_Object = MibTableColumn
nndsxT1E1IfItutArchiveStatsBBE = _NndsxT1E1IfItutArchiveStatsBBE_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3, 1, 4),
    _NndsxT1E1IfItutArchiveStatsBBE_Type()
)
nndsxT1E1IfItutArchiveStatsBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsBBE.setStatus("current")
_NndsxT1E1IfItutArchiveStatsSES_Type = Unsigned32
_NndsxT1E1IfItutArchiveStatsSES_Object = MibTableColumn
nndsxT1E1IfItutArchiveStatsSES = _NndsxT1E1IfItutArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 4, 3, 1, 5),
    _NndsxT1E1IfItutArchiveStatsSES_Type()
)
nndsxT1E1IfItutArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfItutArchiveStatsSES.setStatus("current")
_NndsxT1E1IfIetfStatsGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfIetfStatsGroup = _NndsxT1E1IfIetfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5)
)
_NndsxT1E1IfIetfCurrentStatsTable_Object = MibTable
nndsxT1E1IfIetfCurrentStatsTable = _NndsxT1E1IfIetfCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsTable.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsEntry_Object = MibTableRow
nndsxT1E1IfIetfCurrentStatsEntry = _NndsxT1E1IfIetfCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsEntry.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsUASState_Type = TruthValue
_NndsxT1E1IfIetfCurrentStatsUASState_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsUASState = _NndsxT1E1IfIetfCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 1),
    _NndsxT1E1IfIetfCurrentStatsUASState_Type()
)
nndsxT1E1IfIetfCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsUASState.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsTimeInCurrent_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsTimeInCurrent_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsTimeInCurrent = _NndsxT1E1IfIetfCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 2),
    _NndsxT1E1IfIetfCurrentStatsTimeInCurrent_Type()
)
nndsxT1E1IfIetfCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsTimeInCurrent.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsES_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsES_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsES = _NndsxT1E1IfIetfCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 3),
    _NndsxT1E1IfIetfCurrentStatsES_Type()
)
nndsxT1E1IfIetfCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsES.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsSES_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsSES_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsSES = _NndsxT1E1IfIetfCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 4),
    _NndsxT1E1IfIetfCurrentStatsSES_Type()
)
nndsxT1E1IfIetfCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsSES.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsSEFS_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsSEFS_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsSEFS = _NndsxT1E1IfIetfCurrentStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 5),
    _NndsxT1E1IfIetfCurrentStatsSEFS_Type()
)
nndsxT1E1IfIetfCurrentStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsSEFS.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsUAS_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsUAS_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsUAS = _NndsxT1E1IfIetfCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 6),
    _NndsxT1E1IfIetfCurrentStatsUAS_Type()
)
nndsxT1E1IfIetfCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsUAS.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsCSS_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsCSS_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsCSS = _NndsxT1E1IfIetfCurrentStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 7),
    _NndsxT1E1IfIetfCurrentStatsCSS_Type()
)
nndsxT1E1IfIetfCurrentStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsCSS.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsPCV_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsPCV_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsPCV = _NndsxT1E1IfIetfCurrentStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 8),
    _NndsxT1E1IfIetfCurrentStatsPCV_Type()
)
nndsxT1E1IfIetfCurrentStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsPCV.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsLES_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsLES_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsLES = _NndsxT1E1IfIetfCurrentStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 9),
    _NndsxT1E1IfIetfCurrentStatsLES_Type()
)
nndsxT1E1IfIetfCurrentStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsLES.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsBES_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsBES_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsBES = _NndsxT1E1IfIetfCurrentStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 10),
    _NndsxT1E1IfIetfCurrentStatsBES_Type()
)
nndsxT1E1IfIetfCurrentStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsBES.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsDM_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsDM_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsDM = _NndsxT1E1IfIetfCurrentStatsDM_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 11),
    _NndsxT1E1IfIetfCurrentStatsDM_Type()
)
nndsxT1E1IfIetfCurrentStatsDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsDM.setStatus("current")
_NndsxT1E1IfIetfCurrentStatsLCV_Type = Unsigned32
_NndsxT1E1IfIetfCurrentStatsLCV_Object = MibTableColumn
nndsxT1E1IfIetfCurrentStatsLCV = _NndsxT1E1IfIetfCurrentStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 1, 1, 12),
    _NndsxT1E1IfIetfCurrentStatsLCV_Type()
)
nndsxT1E1IfIetfCurrentStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfCurrentStatsLCV.setStatus("current")
_NndsxT1E1IfIetfTotalStatsTable_Object = MibTable
nndsxT1E1IfIetfTotalStatsTable = _NndsxT1E1IfIetfTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsTable.setStatus("current")
_NndsxT1E1IfIetfTotalStatsEntry_Object = MibTableRow
nndsxT1E1IfIetfTotalStatsEntry = _NndsxT1E1IfIetfTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsEntry.setStatus("current")
_NndsxT1E1IfIetfTotalStatsES_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsES_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsES = _NndsxT1E1IfIetfTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 1),
    _NndsxT1E1IfIetfTotalStatsES_Type()
)
nndsxT1E1IfIetfTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsES.setStatus("current")
_NndsxT1E1IfIetfTotalStatsSES_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsSES_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsSES = _NndsxT1E1IfIetfTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 2),
    _NndsxT1E1IfIetfTotalStatsSES_Type()
)
nndsxT1E1IfIetfTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsSES.setStatus("current")
_NndsxT1E1IfIetfTotalStatsSEFS_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsSEFS_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsSEFS = _NndsxT1E1IfIetfTotalStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 3),
    _NndsxT1E1IfIetfTotalStatsSEFS_Type()
)
nndsxT1E1IfIetfTotalStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsSEFS.setStatus("current")
_NndsxT1E1IfIetfTotalStatsUAS_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsUAS_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsUAS = _NndsxT1E1IfIetfTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 4),
    _NndsxT1E1IfIetfTotalStatsUAS_Type()
)
nndsxT1E1IfIetfTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsUAS.setStatus("current")
_NndsxT1E1IfIetfTotalStatsCSS_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsCSS_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsCSS = _NndsxT1E1IfIetfTotalStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 5),
    _NndsxT1E1IfIetfTotalStatsCSS_Type()
)
nndsxT1E1IfIetfTotalStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsCSS.setStatus("current")
_NndsxT1E1IfIetfTotalStatsPCV_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsPCV_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsPCV = _NndsxT1E1IfIetfTotalStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 6),
    _NndsxT1E1IfIetfTotalStatsPCV_Type()
)
nndsxT1E1IfIetfTotalStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsPCV.setStatus("current")
_NndsxT1E1IfIetfTotalStatsLES_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsLES_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsLES = _NndsxT1E1IfIetfTotalStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 7),
    _NndsxT1E1IfIetfTotalStatsLES_Type()
)
nndsxT1E1IfIetfTotalStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsLES.setStatus("current")
_NndsxT1E1IfIetfTotalStatsBES_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsBES_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsBES = _NndsxT1E1IfIetfTotalStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 8),
    _NndsxT1E1IfIetfTotalStatsBES_Type()
)
nndsxT1E1IfIetfTotalStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsBES.setStatus("current")
_NndsxT1E1IfIetfTotalStatsDM_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsDM_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsDM = _NndsxT1E1IfIetfTotalStatsDM_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 9),
    _NndsxT1E1IfIetfTotalStatsDM_Type()
)
nndsxT1E1IfIetfTotalStatsDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsDM.setStatus("current")
_NndsxT1E1IfIetfTotalStatsLCV_Type = Unsigned32
_NndsxT1E1IfIetfTotalStatsLCV_Object = MibTableColumn
nndsxT1E1IfIetfTotalStatsLCV = _NndsxT1E1IfIetfTotalStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 2, 1, 10),
    _NndsxT1E1IfIetfTotalStatsLCV_Type()
)
nndsxT1E1IfIetfTotalStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfTotalStatsLCV.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsTable_Object = MibTable
nndsxT1E1IfIetfArchiveStatsTable = _NndsxT1E1IfIetfArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsTable.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsEntry_Object = MibTableRow
nndsxT1E1IfIetfArchiveStatsEntry = _NndsxT1E1IfIetfArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1)
)
nndsxT1E1IfIetfArchiveStatsEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIetfArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsEntry.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsInterval_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsInterval_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsInterval = _NndsxT1E1IfIetfArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 1),
    _NndsxT1E1IfIetfArchiveStatsInterval_Type()
)
nndsxT1E1IfIetfArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsInterval.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsES_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsES_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsES = _NndsxT1E1IfIetfArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 2),
    _NndsxT1E1IfIetfArchiveStatsES_Type()
)
nndsxT1E1IfIetfArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsES.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsSES_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsSES_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsSES = _NndsxT1E1IfIetfArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 3),
    _NndsxT1E1IfIetfArchiveStatsSES_Type()
)
nndsxT1E1IfIetfArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsSES.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsSEFS_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsSEFS_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsSEFS = _NndsxT1E1IfIetfArchiveStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 4),
    _NndsxT1E1IfIetfArchiveStatsSEFS_Type()
)
nndsxT1E1IfIetfArchiveStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsSEFS.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsUAS_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsUAS_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsUAS = _NndsxT1E1IfIetfArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 5),
    _NndsxT1E1IfIetfArchiveStatsUAS_Type()
)
nndsxT1E1IfIetfArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsUAS.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsCSS_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsCSS_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsCSS = _NndsxT1E1IfIetfArchiveStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 6),
    _NndsxT1E1IfIetfArchiveStatsCSS_Type()
)
nndsxT1E1IfIetfArchiveStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsCSS.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsPCV_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsPCV_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsPCV = _NndsxT1E1IfIetfArchiveStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 7),
    _NndsxT1E1IfIetfArchiveStatsPCV_Type()
)
nndsxT1E1IfIetfArchiveStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsPCV.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsLES_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsLES_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsLES = _NndsxT1E1IfIetfArchiveStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 8),
    _NndsxT1E1IfIetfArchiveStatsLES_Type()
)
nndsxT1E1IfIetfArchiveStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsLES.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsBES_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsBES_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsBES = _NndsxT1E1IfIetfArchiveStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 9),
    _NndsxT1E1IfIetfArchiveStatsBES_Type()
)
nndsxT1E1IfIetfArchiveStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsBES.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsDM_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsDM_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsDM = _NndsxT1E1IfIetfArchiveStatsDM_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 10),
    _NndsxT1E1IfIetfArchiveStatsDM_Type()
)
nndsxT1E1IfIetfArchiveStatsDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsDM.setStatus("current")
_NndsxT1E1IfIetfArchiveStatsLCV_Type = Unsigned32
_NndsxT1E1IfIetfArchiveStatsLCV_Object = MibTableColumn
nndsxT1E1IfIetfArchiveStatsLCV = _NndsxT1E1IfIetfArchiveStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 5, 3, 1, 11),
    _NndsxT1E1IfIetfArchiveStatsLCV_Type()
)
nndsxT1E1IfIetfArchiveStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfIetfArchiveStatsLCV.setStatus("current")
_NndsxT1E1IfUserStatsGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfUserStatsGroup = _NndsxT1E1IfUserStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6)
)
_NndsxT1E1IfUserCurrentStatsTable_Object = MibTable
nndsxT1E1IfUserCurrentStatsTable = _NndsxT1E1IfUserCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsTable.setStatus("current")
_NndsxT1E1IfUserCurrentStatsEntry_Object = MibTableRow
nndsxT1E1IfUserCurrentStatsEntry = _NndsxT1E1IfUserCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsEntry.setStatus("current")
_NndsxT1E1IfUserCurrentStatsUASState_Type = TruthValue
_NndsxT1E1IfUserCurrentStatsUASState_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsUASState = _NndsxT1E1IfUserCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 1),
    _NndsxT1E1IfUserCurrentStatsUASState_Type()
)
nndsxT1E1IfUserCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsUASState.setStatus("current")
_NndsxT1E1IfUserCurrentStatsTimeInCurrent_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsTimeInCurrent_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsTimeInCurrent = _NndsxT1E1IfUserCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 2),
    _NndsxT1E1IfUserCurrentStatsTimeInCurrent_Type()
)
nndsxT1E1IfUserCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsTimeInCurrent.setStatus("current")
_NndsxT1E1IfUserCurrentStatsEEV_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsEEV_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsEEV = _NndsxT1E1IfUserCurrentStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 3),
    _NndsxT1E1IfUserCurrentStatsEEV_Type()
)
nndsxT1E1IfUserCurrentStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsEEV.setStatus("current")
_NndsxT1E1IfUserCurrentStatsES_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsES_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsES = _NndsxT1E1IfUserCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 4),
    _NndsxT1E1IfUserCurrentStatsES_Type()
)
nndsxT1E1IfUserCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsES.setStatus("current")
_NndsxT1E1IfUserCurrentStatsUAS_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsUAS_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsUAS = _NndsxT1E1IfUserCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 5),
    _NndsxT1E1IfUserCurrentStatsUAS_Type()
)
nndsxT1E1IfUserCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsUAS.setStatus("current")
_NndsxT1E1IfUserCurrentStatsBES_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsBES_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsBES = _NndsxT1E1IfUserCurrentStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 6),
    _NndsxT1E1IfUserCurrentStatsBES_Type()
)
nndsxT1E1IfUserCurrentStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsBES.setStatus("current")
_NndsxT1E1IfUserCurrentStatsSES_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsSES_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsSES = _NndsxT1E1IfUserCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 7),
    _NndsxT1E1IfUserCurrentStatsSES_Type()
)
nndsxT1E1IfUserCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsSES.setStatus("current")
_NndsxT1E1IfUserCurrentStatsLOFC_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsLOFC_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsLOFC = _NndsxT1E1IfUserCurrentStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 8),
    _NndsxT1E1IfUserCurrentStatsLOFC_Type()
)
nndsxT1E1IfUserCurrentStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsLOFC.setStatus("current")
_NndsxT1E1IfUserCurrentStatsCSS_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsCSS_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsCSS = _NndsxT1E1IfUserCurrentStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 9),
    _NndsxT1E1IfUserCurrentStatsCSS_Type()
)
nndsxT1E1IfUserCurrentStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsCSS.setStatus("current")
_NndsxT1E1IfUserCurrentStatsBPV_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsBPV_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsBPV = _NndsxT1E1IfUserCurrentStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 10),
    _NndsxT1E1IfUserCurrentStatsBPV_Type()
)
nndsxT1E1IfUserCurrentStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsBPV.setStatus("current")
_NndsxT1E1IfUserCurrentStatsOOF_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsOOF_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsOOF = _NndsxT1E1IfUserCurrentStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 11),
    _NndsxT1E1IfUserCurrentStatsOOF_Type()
)
nndsxT1E1IfUserCurrentStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsOOF.setStatus("current")
_NndsxT1E1IfUserCurrentStatsCRC_Type = Unsigned32
_NndsxT1E1IfUserCurrentStatsCRC_Object = MibTableColumn
nndsxT1E1IfUserCurrentStatsCRC = _NndsxT1E1IfUserCurrentStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 1, 1, 12),
    _NndsxT1E1IfUserCurrentStatsCRC_Type()
)
nndsxT1E1IfUserCurrentStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserCurrentStatsCRC.setStatus("current")
_NndsxT1E1IfUserTotalStatsTable_Object = MibTable
nndsxT1E1IfUserTotalStatsTable = _NndsxT1E1IfUserTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsTable.setStatus("current")
_NndsxT1E1IfUserTotalStatsEntry_Object = MibTableRow
nndsxT1E1IfUserTotalStatsEntry = _NndsxT1E1IfUserTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1)
)
nndsxT1E1IfUserTotalStatsEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfUserTotalStatsDay"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsEntry.setStatus("current")
_NndsxT1E1IfUserTotalStatsDay_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsDay_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsDay = _NndsxT1E1IfUserTotalStatsDay_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 1),
    _NndsxT1E1IfUserTotalStatsDay_Type()
)
nndsxT1E1IfUserTotalStatsDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsDay.setStatus("current")
_NndsxT1E1IfUserTotalStatsEEV_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsEEV_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsEEV = _NndsxT1E1IfUserTotalStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 2),
    _NndsxT1E1IfUserTotalStatsEEV_Type()
)
nndsxT1E1IfUserTotalStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsEEV.setStatus("current")
_NndsxT1E1IfUserTotalStatsES_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsES_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsES = _NndsxT1E1IfUserTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 3),
    _NndsxT1E1IfUserTotalStatsES_Type()
)
nndsxT1E1IfUserTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsES.setStatus("current")
_NndsxT1E1IfUserTotalStatsUAS_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsUAS_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsUAS = _NndsxT1E1IfUserTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 4),
    _NndsxT1E1IfUserTotalStatsUAS_Type()
)
nndsxT1E1IfUserTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsUAS.setStatus("current")
_NndsxT1E1IfUserTotalStatsBES_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsBES_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsBES = _NndsxT1E1IfUserTotalStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 5),
    _NndsxT1E1IfUserTotalStatsBES_Type()
)
nndsxT1E1IfUserTotalStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsBES.setStatus("current")
_NndsxT1E1IfUserTotalStatsSES_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsSES_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsSES = _NndsxT1E1IfUserTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 6),
    _NndsxT1E1IfUserTotalStatsSES_Type()
)
nndsxT1E1IfUserTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsSES.setStatus("current")
_NndsxT1E1IfUserTotalStatsLOFC_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsLOFC_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsLOFC = _NndsxT1E1IfUserTotalStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 7),
    _NndsxT1E1IfUserTotalStatsLOFC_Type()
)
nndsxT1E1IfUserTotalStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsLOFC.setStatus("current")
_NndsxT1E1IfUserTotalStatsCSS_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsCSS_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsCSS = _NndsxT1E1IfUserTotalStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 8),
    _NndsxT1E1IfUserTotalStatsCSS_Type()
)
nndsxT1E1IfUserTotalStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsCSS.setStatus("current")
_NndsxT1E1IfUserTotalStatsBPV_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsBPV_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsBPV = _NndsxT1E1IfUserTotalStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 9),
    _NndsxT1E1IfUserTotalStatsBPV_Type()
)
nndsxT1E1IfUserTotalStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsBPV.setStatus("current")
_NndsxT1E1IfUserTotalStatsOOF_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsOOF_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsOOF = _NndsxT1E1IfUserTotalStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 10),
    _NndsxT1E1IfUserTotalStatsOOF_Type()
)
nndsxT1E1IfUserTotalStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsOOF.setStatus("current")
_NndsxT1E1IfUserTotalStatsCRC_Type = Unsigned32
_NndsxT1E1IfUserTotalStatsCRC_Object = MibTableColumn
nndsxT1E1IfUserTotalStatsCRC = _NndsxT1E1IfUserTotalStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 2, 1, 11),
    _NndsxT1E1IfUserTotalStatsCRC_Type()
)
nndsxT1E1IfUserTotalStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserTotalStatsCRC.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsTable_Object = MibTable
nndsxT1E1IfUserLifetimeStatsTable = _NndsxT1E1IfUserLifetimeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsTable.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsEntry_Object = MibTableRow
nndsxT1E1IfUserLifetimeStatsEntry = _NndsxT1E1IfUserLifetimeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsEntry.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsEEV_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsEEV_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsEEV = _NndsxT1E1IfUserLifetimeStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 1),
    _NndsxT1E1IfUserLifetimeStatsEEV_Type()
)
nndsxT1E1IfUserLifetimeStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsEEV.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsES_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsES_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsES = _NndsxT1E1IfUserLifetimeStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 2),
    _NndsxT1E1IfUserLifetimeStatsES_Type()
)
nndsxT1E1IfUserLifetimeStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsES.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsUAS_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsUAS_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsUAS = _NndsxT1E1IfUserLifetimeStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 3),
    _NndsxT1E1IfUserLifetimeStatsUAS_Type()
)
nndsxT1E1IfUserLifetimeStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsUAS.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsBES_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsBES_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsBES = _NndsxT1E1IfUserLifetimeStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 4),
    _NndsxT1E1IfUserLifetimeStatsBES_Type()
)
nndsxT1E1IfUserLifetimeStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsBES.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsSES_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsSES_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsSES = _NndsxT1E1IfUserLifetimeStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 5),
    _NndsxT1E1IfUserLifetimeStatsSES_Type()
)
nndsxT1E1IfUserLifetimeStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsSES.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsLOFC_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsLOFC_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsLOFC = _NndsxT1E1IfUserLifetimeStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 6),
    _NndsxT1E1IfUserLifetimeStatsLOFC_Type()
)
nndsxT1E1IfUserLifetimeStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsLOFC.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsCSS_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsCSS_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsCSS = _NndsxT1E1IfUserLifetimeStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 7),
    _NndsxT1E1IfUserLifetimeStatsCSS_Type()
)
nndsxT1E1IfUserLifetimeStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsCSS.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsBPV_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsBPV_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsBPV = _NndsxT1E1IfUserLifetimeStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 8),
    _NndsxT1E1IfUserLifetimeStatsBPV_Type()
)
nndsxT1E1IfUserLifetimeStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsBPV.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsOOF_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsOOF_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsOOF = _NndsxT1E1IfUserLifetimeStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 9),
    _NndsxT1E1IfUserLifetimeStatsOOF_Type()
)
nndsxT1E1IfUserLifetimeStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsOOF.setStatus("current")
_NndsxT1E1IfUserLifetimeStatsCRC_Type = Unsigned32
_NndsxT1E1IfUserLifetimeStatsCRC_Object = MibTableColumn
nndsxT1E1IfUserLifetimeStatsCRC = _NndsxT1E1IfUserLifetimeStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 3, 1, 10),
    _NndsxT1E1IfUserLifetimeStatsCRC_Type()
)
nndsxT1E1IfUserLifetimeStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserLifetimeStatsCRC.setStatus("current")
_NndsxT1E1IfUserArchiveStatsTable_Object = MibTable
nndsxT1E1IfUserArchiveStatsTable = _NndsxT1E1IfUserArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4)
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsTable.setStatus("current")
_NndsxT1E1IfUserArchiveStatsEntry_Object = MibTableRow
nndsxT1E1IfUserArchiveStatsEntry = _NndsxT1E1IfUserArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1)
)
nndsxT1E1IfUserArchiveStatsEntry.setIndexNames(
    (0, "DSX-TE1-MIB", "nndsxT1E1IfIndex"),
    (0, "DSX-TE1-MIB", "nndsxT1E1IfUserArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsEntry.setStatus("current")
_NndsxT1E1IfUserArchiveStatsInterval_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsInterval_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsInterval = _NndsxT1E1IfUserArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 1),
    _NndsxT1E1IfUserArchiveStatsInterval_Type()
)
nndsxT1E1IfUserArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsInterval.setStatus("current")
_NndsxT1E1IfUserArchiveStatsEEV_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsEEV_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsEEV = _NndsxT1E1IfUserArchiveStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 2),
    _NndsxT1E1IfUserArchiveStatsEEV_Type()
)
nndsxT1E1IfUserArchiveStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsEEV.setStatus("current")
_NndsxT1E1IfUserArchiveStatsES_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsES_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsES = _NndsxT1E1IfUserArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 3),
    _NndsxT1E1IfUserArchiveStatsES_Type()
)
nndsxT1E1IfUserArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsES.setStatus("current")
_NndsxT1E1IfUserArchiveStatsUAS_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsUAS_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsUAS = _NndsxT1E1IfUserArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 4),
    _NndsxT1E1IfUserArchiveStatsUAS_Type()
)
nndsxT1E1IfUserArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsUAS.setStatus("current")
_NndsxT1E1IfUserArchiveStatsBES_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsBES_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsBES = _NndsxT1E1IfUserArchiveStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 5),
    _NndsxT1E1IfUserArchiveStatsBES_Type()
)
nndsxT1E1IfUserArchiveStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsBES.setStatus("current")
_NndsxT1E1IfUserArchiveStatsSES_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsSES_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsSES = _NndsxT1E1IfUserArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 6),
    _NndsxT1E1IfUserArchiveStatsSES_Type()
)
nndsxT1E1IfUserArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsSES.setStatus("current")
_NndsxT1E1IfUserArchiveStatsLOFC_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsLOFC_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsLOFC = _NndsxT1E1IfUserArchiveStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 7),
    _NndsxT1E1IfUserArchiveStatsLOFC_Type()
)
nndsxT1E1IfUserArchiveStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsLOFC.setStatus("current")
_NndsxT1E1IfUserArchiveStatsCSS_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsCSS_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsCSS = _NndsxT1E1IfUserArchiveStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 8),
    _NndsxT1E1IfUserArchiveStatsCSS_Type()
)
nndsxT1E1IfUserArchiveStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsCSS.setStatus("current")
_NndsxT1E1IfUserArchiveStatsBPV_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsBPV_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsBPV = _NndsxT1E1IfUserArchiveStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 9),
    _NndsxT1E1IfUserArchiveStatsBPV_Type()
)
nndsxT1E1IfUserArchiveStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsBPV.setStatus("current")
_NndsxT1E1IfUserArchiveStatsOOF_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsOOF_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsOOF = _NndsxT1E1IfUserArchiveStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 10),
    _NndsxT1E1IfUserArchiveStatsOOF_Type()
)
nndsxT1E1IfUserArchiveStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsOOF.setStatus("current")
_NndsxT1E1IfUserArchiveStatsCRC_Type = Unsigned32
_NndsxT1E1IfUserArchiveStatsCRC_Object = MibTableColumn
nndsxT1E1IfUserArchiveStatsCRC = _NndsxT1E1IfUserArchiveStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 1, 3, 6, 4, 1, 11),
    _NndsxT1E1IfUserArchiveStatsCRC_Type()
)
nndsxT1E1IfUserArchiveStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nndsxT1E1IfUserArchiveStatsCRC.setStatus("current")
_NndsxT1E1Traps_ObjectIdentity = ObjectIdentity
nndsxT1E1Traps = _NndsxT1E1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2)
)
_NndsxT1E1Notifications_ObjectIdentity = ObjectIdentity
nndsxT1E1Notifications = _NndsxT1E1Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 0)
)
_NndsxT1E1TrapVariables_ObjectIdentity = ObjectIdentity
nndsxT1E1TrapVariables = _NndsxT1E1TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 1)
)


class _NndsxT1E1Number_Type(DisplayString):
    """Custom type nndsxT1E1Number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NndsxT1E1Number_Type.__name__ = "DisplayString"
_NndsxT1E1Number_Object = MibScalar
nndsxT1E1Number = _NndsxT1E1Number_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 1, 1),
    _NndsxT1E1Number_Type()
)
nndsxT1E1Number.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nndsxT1E1Number.setStatus("current")


class _NndsxT1E1Type_Type(Integer32):
    """Custom type nndsxT1E1Type based on Integer32"""
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
        *(("type-e1", 3),
          ("type-e1-within-ce3", 4),
          ("type-t1", 1),
          ("type-t1-within-ct3", 2))
    )


_NndsxT1E1Type_Type.__name__ = "Integer32"
_NndsxT1E1Type_Object = MibScalar
nndsxT1E1Type = _NndsxT1E1Type_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 1, 2),
    _NndsxT1E1Type_Type()
)
nndsxT1E1Type.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nndsxT1E1Type.setStatus("current")


class _NndsxT1E1T3Number_Type(DisplayString):
    """Custom type nndsxT1E1T3Number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NndsxT1E1T3Number_Type.__name__ = "DisplayString"
_NndsxT1E1T3Number_Object = MibScalar
nndsxT1E1T3Number = _NndsxT1E1T3Number_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 1, 3),
    _NndsxT1E1T3Number_Type()
)
nndsxT1E1T3Number.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nndsxT1E1T3Number.setStatus("current")


class _NndsxT1E1AlarmType_Type(Integer32):
    """Custom type nndsxT1E1AlarmType based on Integer32"""
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
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("te1-alarm-ibtest", 13),
          ("te1-alarm-lorc", 8),
          ("te1-alarm-rais", 1),
          ("te1-alarm-rexz", 6),
          ("te1-alarm-rfbe", 7),
          ("te1-alarm-rlof", 5),
          ("te1-alarm-rlos", 4),
          ("te1-alarm-roof", 3),
          ("te1-alarm-rrai", 2),
          ("te1-alarm-tais", 10),
          ("te1-alarm-tblu", 11),
          ("te1-alarm-threshold1", 14),
          ("te1-alarm-threshold10", 23),
          ("te1-alarm-threshold2", 15),
          ("te1-alarm-threshold3", 16),
          ("te1-alarm-threshold4", 17),
          ("te1-alarm-threshold5", 18),
          ("te1-alarm-threshold6", 19),
          ("te1-alarm-threshold7", 20),
          ("te1-alarm-threshold8", 21),
          ("te1-alarm-threshold9", 22),
          ("te1-alarm-tpde", 9),
          ("te1-alarm-trai", 12))
    )


_NndsxT1E1AlarmType_Type.__name__ = "Integer32"
_NndsxT1E1AlarmType_Object = MibScalar
nndsxT1E1AlarmType = _NndsxT1E1AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 1, 4),
    _NndsxT1E1AlarmType_Type()
)
nndsxT1E1AlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nndsxT1E1AlarmType.setStatus("current")
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfConfigFdlEntry")
)
nndsxT1E1IfConfigFdlEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfTestConfigEntry")
)
nndsxT1E1IfTestConfigEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfStatusEntry")
)
nndsxT1E1IfStatusEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfAlarmStatusEntry")
)
nndsxT1E1IfAlarmStatusEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfTestStatusEntry")
)
nndsxT1E1IfTestStatusEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfLastTestResultEntry")
)
nndsxT1E1IfLastTestResultEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfArchiveStatsValidIntervalsEntry")
)
nndsxT1E1IfArchiveStatsValidIntervalsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfAnsiCurrentStatsEntry")
)
nndsxT1E1IfAnsiCurrentStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfAnsiTotalStatsEntry")
)
nndsxT1E1IfAnsiTotalStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfAttCurrentStatsEntry")
)
nndsxT1E1IfAttCurrentStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfAttTotalStatsEntry")
)
nndsxT1E1IfAttTotalStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfItutCurrentStatsEntry")
)
nndsxT1E1IfItutCurrentStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfItutTotalStatsEntry")
)
nndsxT1E1IfItutTotalStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfIetfCurrentStatsEntry")
)
nndsxT1E1IfIetfCurrentStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfIetfTotalStatsEntry")
)
nndsxT1E1IfIetfTotalStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfUserCurrentStatsEntry")
)
nndsxT1E1IfUserCurrentStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())
nndsxT1E1IfConfigLineEntry.registerAugmentions(
    ("DSX-TE1-MIB",
     "nndsxT1E1IfUserLifetimeStatsEntry")
)
nndsxT1E1IfUserLifetimeStatsEntry.setIndexNames(*nndsxT1E1IfConfigLineEntry.getIndexNames())

# Managed Objects groups


# Notification objects

nndsxT1E1AlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 0, 1)
)
nndsxT1E1AlarmOnTrap.setObjects(
      *(("DSX-TE1-MIB", "nndsxT1E1IfIndex"),
        ("DSX-TE1-MIB", "nndsxT1E1Number"),
        ("DSX-TE1-MIB", "nndsxT1E1Type"),
        ("DSX-TE1-MIB", "nndsxT1E1T3Number"),
        ("DSX-TE1-MIB", "nndsxT1E1AlarmType"))
)
if mibBuilder.loadTexts:
    nndsxT1E1AlarmOnTrap.setStatus(
        "current"
    )

nndsxT1E1AlarmOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 2, 0, 2)
)
nndsxT1E1AlarmOffTrap.setObjects(
      *(("DSX-TE1-MIB", "nndsxT1E1IfIndex"),
        ("DSX-TE1-MIB", "nndsxT1E1Number"),
        ("DSX-TE1-MIB", "nndsxT1E1Type"),
        ("DSX-TE1-MIB", "nndsxT1E1T3Number"),
        ("DSX-TE1-MIB", "nndsxT1E1AlarmType"))
)
if mibBuilder.loadTexts:
    nndsxT1E1AlarmOffTrap.setStatus(
        "current"
    )


# Notifications groups

nndsxT1E1NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2, 3)
)
nndsxT1E1NotificationGroup.setObjects(
      *(("DSX-TE1-MIB", "nndsxT1E1AlarmOnTrap"),
        ("DSX-TE1-MIB", "nndsxT1E1AlarmOffTrap"))
)
if mibBuilder.loadTexts:
    nndsxT1E1NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSX-TE1-MIB",
    **{"nndsxT1E1MIB": nndsxT1E1MIB,
       "nndsxT1E1IfConfigGroup": nndsxT1E1IfConfigGroup,
       "nndsxT1E1IfConfigLineTable": nndsxT1E1IfConfigLineTable,
       "nndsxT1E1IfConfigLineEntry": nndsxT1E1IfConfigLineEntry,
       "nndsxT1E1IfIndex": nndsxT1E1IfIndex,
       "nndsxT1E1IfConfigServiceMode": nndsxT1E1IfConfigServiceMode,
       "nndsxT1E1IfConfigLineMode": nndsxT1E1IfConfigLineMode,
       "nndsxT1E1IfConfigLineType": nndsxT1E1IfConfigLineType,
       "nndsxT1E1IfConfigLineCode": nndsxT1E1IfConfigLineCode,
       "nndsxT1E1IfConfigLBO": nndsxT1E1IfConfigLBO,
       "nndsxT1E1IfConfigCableLength": nndsxT1E1IfConfigCableLength,
       "nndsxT1E1IfConfigRaiAlarm": nndsxT1E1IfConfigRaiAlarm,
       "nndsxT1E1IfConfigTransmitClock": nndsxT1E1IfConfigTransmitClock,
       "nndsxT1E1IfConfigTimeSlotMap": nndsxT1E1IfConfigTimeSlotMap,
       "nndsxT1E1IfConfigCableType": nndsxT1E1IfConfigCableType,
       "nndsxT1E1IfCircuitId": nndsxT1E1IfCircuitId,
       "nndsxT1E1IfContactInfo": nndsxT1E1IfContactInfo,
       "nndsxT1E1IfDescription": nndsxT1E1IfDescription,
       "nndsxT1E1IfConfigJitter": nndsxT1E1IfConfigJitter,
       "nndsxT1E1IfConfigAlarmHierarchy": nndsxT1E1IfConfigAlarmHierarchy,
       "nndsxT1E1IfConfigFdlTable": nndsxT1E1IfConfigFdlTable,
       "nndsxT1E1IfConfigFdlEntry": nndsxT1E1IfConfigFdlEntry,
       "nndsxT1E1IfConfigFdl": nndsxT1E1IfConfigFdl,
       "nndsxT1E1IfConfigFdlCsuDsuType": nndsxT1E1IfConfigFdlCsuDsuType,
       "nndsxT1E1IfAlarmConfigGroup": nndsxT1E1IfAlarmConfigGroup,
       "nndsxT1E1IfAlarmThresholdConfigTable": nndsxT1E1IfAlarmThresholdConfigTable,
       "nndsxT1E1IfAlarmThresholdConfigEntry": nndsxT1E1IfAlarmThresholdConfigEntry,
       "nndsxT1E1IfAlarmThresholdConfigIndex": nndsxT1E1IfAlarmThresholdConfigIndex,
       "nndsxT1E1IfAlarmThresholdConfigObject": nndsxT1E1IfAlarmThresholdConfigObject,
       "nndsxT1E1IfAlarmThresholdConfigSamplingInterval": nndsxT1E1IfAlarmThresholdConfigSamplingInterval,
       "nndsxT1E1IfAlarmThresholdConfigSampleType": nndsxT1E1IfAlarmThresholdConfigSampleType,
       "nndsxT1E1IfAlarmThresholdConfigRisingThreshold": nndsxT1E1IfAlarmThresholdConfigRisingThreshold,
       "nndsxT1E1IfAlarmThresholdConfigFallingThreshold": nndsxT1E1IfAlarmThresholdConfigFallingThreshold,
       "nndsxT1E1IfAlarmThresholdConfigEnable": nndsxT1E1IfAlarmThresholdConfigEnable,
       "nndsxT1E1IfTestConfigTable": nndsxT1E1IfTestConfigTable,
       "nndsxT1E1IfTestConfigEntry": nndsxT1E1IfTestConfigEntry,
       "nndsxT1E1IfTestConfigType": nndsxT1E1IfTestConfigType,
       "nndsxT1E1IfTestConfigTime": nndsxT1E1IfTestConfigTime,
       "nndsxT1E1IfTestConfigPattern": nndsxT1E1IfTestConfigPattern,
       "nndsxT1E1IfTestConfigLoopCode": nndsxT1E1IfTestConfigLoopCode,
       "nndsxT1E1IfMonitorPortConfigType": nndsxT1E1IfMonitorPortConfigType,
       "nndsxT1E1IfMonitorPortTxInjectType": nndsxT1E1IfMonitorPortTxInjectType,
       "nndsxT1E1IfStatusGroup": nndsxT1E1IfStatusGroup,
       "nndsxT1E1IfStatusTable": nndsxT1E1IfStatusTable,
       "nndsxT1E1IfStatusEntry": nndsxT1E1IfStatusEntry,
       "nndsxT1E1IfStatusLineStatus": nndsxT1E1IfStatusLineStatus,
       "nndsxT1E1IfStatusTransmitClock": nndsxT1E1IfStatusTransmitClock,
       "nndsxT1E1IfAlarmStatusTable": nndsxT1E1IfAlarmStatusTable,
       "nndsxT1E1IfAlarmStatusEntry": nndsxT1E1IfAlarmStatusEntry,
       "nndsxT1E1IfAlarmStatusAlarmStatus": nndsxT1E1IfAlarmStatusAlarmStatus,
       "nndsxT1E1IfAlarmStatusThresholdStatus": nndsxT1E1IfAlarmStatusThresholdStatus,
       "nndsxT1E1IfTestStatusTable": nndsxT1E1IfTestStatusTable,
       "nndsxT1E1IfTestStatusEntry": nndsxT1E1IfTestStatusEntry,
       "nndsxT1E1IfTestStatusTestType": nndsxT1E1IfTestStatusTestType,
       "nndsxT1E1IfTestStatusTestTime": nndsxT1E1IfTestStatusTestTime,
       "nndsxT1E1IfTestStatusTestState": nndsxT1E1IfTestStatusTestState,
       "nndsxT1E1IfTestStatusTestPattern": nndsxT1E1IfTestStatusTestPattern,
       "nndsxT1E1IfTestStatusLockedSeconds": nndsxT1E1IfTestStatusLockedSeconds,
       "nndsxT1E1IfTestStatusSyncLossCount": nndsxT1E1IfTestStatusSyncLossCount,
       "nndsxT1E1IfTestStatusErrorCount": nndsxT1E1IfTestStatusErrorCount,
       "nndsxT1E1IfTestStatusLoopCode": nndsxT1E1IfTestStatusLoopCode,
       "nndsxT1E1IfLastTestResultTable": nndsxT1E1IfLastTestResultTable,
       "nndsxT1E1IfLastTestResultEntry": nndsxT1E1IfLastTestResultEntry,
       "nndsxT1E1IfLastTestResultTestType": nndsxT1E1IfLastTestResultTestType,
       "nndsxT1E1IfLastTestResultTestTime": nndsxT1E1IfLastTestResultTestTime,
       "nndsxT1E1IfLastTestResultTestState": nndsxT1E1IfLastTestResultTestState,
       "nndsxT1E1IfLastTestResultTestPattern": nndsxT1E1IfLastTestResultTestPattern,
       "nndsxT1E1IfLastTestResultLockedSeconds": nndsxT1E1IfLastTestResultLockedSeconds,
       "nndsxT1E1IfLastTestResultSyncLossCount": nndsxT1E1IfLastTestResultSyncLossCount,
       "nndsxT1E1IfLastTestResultErrorCount": nndsxT1E1IfLastTestResultErrorCount,
       "nndsxT1E1IfLastTestResultLoopCode": nndsxT1E1IfLastTestResultLoopCode,
       "nndsxT1E1IfStatsGroup": nndsxT1E1IfStatsGroup,
       "nndsxT1E1IfArchiveStatsValidIntervalsTable": nndsxT1E1IfArchiveStatsValidIntervalsTable,
       "nndsxT1E1IfArchiveStatsValidIntervalsEntry": nndsxT1E1IfArchiveStatsValidIntervalsEntry,
       "nndsxT1E1IfAnsiArchiveStatsValidIntervals": nndsxT1E1IfAnsiArchiveStatsValidIntervals,
       "nndsxT1E1IfAttArchiveStatsValidIntervals": nndsxT1E1IfAttArchiveStatsValidIntervals,
       "nndsxT1E1IfItutArchiveStatsValidIntervals": nndsxT1E1IfItutArchiveStatsValidIntervals,
       "nndsxT1E1IfIetfArchiveStatsValidIntervals": nndsxT1E1IfIetfArchiveStatsValidIntervals,
       "nndsxT1E1IfUserTotalStatsValidDays": nndsxT1E1IfUserTotalStatsValidDays,
       "nndsxT1E1IfUserArchiveStatsValidIntervals": nndsxT1E1IfUserArchiveStatsValidIntervals,
       "nndsxT1E1IfAnsiStatsGroup": nndsxT1E1IfAnsiStatsGroup,
       "nndsxT1E1IfAnsiCurrentStatsTable": nndsxT1E1IfAnsiCurrentStatsTable,
       "nndsxT1E1IfAnsiCurrentStatsEntry": nndsxT1E1IfAnsiCurrentStatsEntry,
       "nndsxT1E1IfAnsiCurrentStatsUASState": nndsxT1E1IfAnsiCurrentStatsUASState,
       "nndsxT1E1IfAnsiCurrentStatsTimeInCurrent": nndsxT1E1IfAnsiCurrentStatsTimeInCurrent,
       "nndsxT1E1IfAnsiCurrentPathStatsCV": nndsxT1E1IfAnsiCurrentPathStatsCV,
       "nndsxT1E1IfAnsiCurrentPathStatsES": nndsxT1E1IfAnsiCurrentPathStatsES,
       "nndsxT1E1IfAnsiCurrentPathStatsSES": nndsxT1E1IfAnsiCurrentPathStatsSES,
       "nndsxT1E1IfAnsiCurrentPathStatsSAS": nndsxT1E1IfAnsiCurrentPathStatsSAS,
       "nndsxT1E1IfAnsiCurrentPathStatsCSS": nndsxT1E1IfAnsiCurrentPathStatsCSS,
       "nndsxT1E1IfAnsiCurrentPathStatsUAS": nndsxT1E1IfAnsiCurrentPathStatsUAS,
       "nndsxT1E1IfAnsiCurrentLineStatsCV": nndsxT1E1IfAnsiCurrentLineStatsCV,
       "nndsxT1E1IfAnsiCurrentLineStatsES": nndsxT1E1IfAnsiCurrentLineStatsES,
       "nndsxT1E1IfAnsiCurrentLineStatsSES": nndsxT1E1IfAnsiCurrentLineStatsSES,
       "nndsxT1E1IfAnsiTotalStatsTable": nndsxT1E1IfAnsiTotalStatsTable,
       "nndsxT1E1IfAnsiTotalStatsEntry": nndsxT1E1IfAnsiTotalStatsEntry,
       "nndsxT1E1IfAnsiTotalPathStatsCV": nndsxT1E1IfAnsiTotalPathStatsCV,
       "nndsxT1E1IfAnsiTotalPathStatsES": nndsxT1E1IfAnsiTotalPathStatsES,
       "nndsxT1E1IfAnsiTotalPathStatsSES": nndsxT1E1IfAnsiTotalPathStatsSES,
       "nndsxT1E1IfAnsiTotalPathStatsSAS": nndsxT1E1IfAnsiTotalPathStatsSAS,
       "nndsxT1E1IfAnsiTotalPathStatsCSS": nndsxT1E1IfAnsiTotalPathStatsCSS,
       "nndsxT1E1IfAnsiTotalPathStatsUAS": nndsxT1E1IfAnsiTotalPathStatsUAS,
       "nndsxT1E1IfAnsiTotalLineStatsCV": nndsxT1E1IfAnsiTotalLineStatsCV,
       "nndsxT1E1IfAnsiTotalLineStatsES": nndsxT1E1IfAnsiTotalLineStatsES,
       "nndsxT1E1IfAnsiTotalLineStatsSES": nndsxT1E1IfAnsiTotalLineStatsSES,
       "nndsxT1E1IfAnsiArchiveIntervalStatsTable": nndsxT1E1IfAnsiArchiveIntervalStatsTable,
       "nndsxT1E1IfAnsiArchiveIntervalStatsEntry": nndsxT1E1IfAnsiArchiveIntervalStatsEntry,
       "nndsxT1E1IfAnsiArchiveStatsInterval": nndsxT1E1IfAnsiArchiveStatsInterval,
       "nndsxT1E1IfAnsiArchiveIntervalPathStatsCV": nndsxT1E1IfAnsiArchiveIntervalPathStatsCV,
       "nndsxT1E1IfAnsiArchiveIntervalPathStatsES": nndsxT1E1IfAnsiArchiveIntervalPathStatsES,
       "nndsxT1E1IfAnsiArchiveIntervalPathStatsSES": nndsxT1E1IfAnsiArchiveIntervalPathStatsSES,
       "nndsxT1E1IfAnsiArchiveIntervalPathStatsSAS": nndsxT1E1IfAnsiArchiveIntervalPathStatsSAS,
       "nndsxT1E1IfAnsiArchiveIntervalPathStatsCSS": nndsxT1E1IfAnsiArchiveIntervalPathStatsCSS,
       "nndsxT1E1IfAnsiArchiveIntervalPathStatsUAS": nndsxT1E1IfAnsiArchiveIntervalPathStatsUAS,
       "nndsxT1E1IfAnsiArchiveIntervalLineStatsCV": nndsxT1E1IfAnsiArchiveIntervalLineStatsCV,
       "nndsxT1E1IfAnsiArchiveIntervalLineStatsES": nndsxT1E1IfAnsiArchiveIntervalLineStatsES,
       "nndsxT1E1IfAnsiArchiveIntervalLineStatsSES": nndsxT1E1IfAnsiArchiveIntervalLineStatsSES,
       "nndsxT1E1IfAttStatsGroup": nndsxT1E1IfAttStatsGroup,
       "nndsxT1E1IfAttCurrentStatsTable": nndsxT1E1IfAttCurrentStatsTable,
       "nndsxT1E1IfAttCurrentStatsEntry": nndsxT1E1IfAttCurrentStatsEntry,
       "nndsxT1E1IfAttCurrentStatsUASState": nndsxT1E1IfAttCurrentStatsUASState,
       "nndsxT1E1IfAttCurrentStatsTimeInCurrent": nndsxT1E1IfAttCurrentStatsTimeInCurrent,
       "nndsxT1E1IfAttCurrentStatsEEV": nndsxT1E1IfAttCurrentStatsEEV,
       "nndsxT1E1IfAttCurrentStatsES": nndsxT1E1IfAttCurrentStatsES,
       "nndsxT1E1IfAttCurrentStatsUAS": nndsxT1E1IfAttCurrentStatsUAS,
       "nndsxT1E1IfAttCurrentStatsSES": nndsxT1E1IfAttCurrentStatsSES,
       "nndsxT1E1IfAttCurrentStatsCSS": nndsxT1E1IfAttCurrentStatsCSS,
       "nndsxT1E1IfAttTotalStatsTable": nndsxT1E1IfAttTotalStatsTable,
       "nndsxT1E1IfAttTotalStatsEntry": nndsxT1E1IfAttTotalStatsEntry,
       "nndsxT1E1IfAttTotalStatsEEV": nndsxT1E1IfAttTotalStatsEEV,
       "nndsxT1E1IfAttTotalStatsES": nndsxT1E1IfAttTotalStatsES,
       "nndsxT1E1IfAttTotalStatsUAS": nndsxT1E1IfAttTotalStatsUAS,
       "nndsxT1E1IfAttTotalStatsSES": nndsxT1E1IfAttTotalStatsSES,
       "nndsxT1E1IfAttTotalStatsCSS": nndsxT1E1IfAttTotalStatsCSS,
       "nndsxT1E1IfAttArchiveStatsTable": nndsxT1E1IfAttArchiveStatsTable,
       "nndsxT1E1IfAttArchiveStatsEntry": nndsxT1E1IfAttArchiveStatsEntry,
       "nndsxT1E1IfAttArchiveInterval": nndsxT1E1IfAttArchiveInterval,
       "nndsxT1E1IfAttArchiveStatsEEV": nndsxT1E1IfAttArchiveStatsEEV,
       "nndsxT1E1IfAttArchiveStatsES": nndsxT1E1IfAttArchiveStatsES,
       "nndsxT1E1IfAttArchiveStatsUAS": nndsxT1E1IfAttArchiveStatsUAS,
       "nndsxT1E1IfAttArchiveStatsSES": nndsxT1E1IfAttArchiveStatsSES,
       "nndsxT1E1IfAttArchiveStatsCSS": nndsxT1E1IfAttArchiveStatsCSS,
       "nndsxT1E1IfItutStatsGroup": nndsxT1E1IfItutStatsGroup,
       "nndsxT1E1IfItutCurrentStatsTable": nndsxT1E1IfItutCurrentStatsTable,
       "nndsxT1E1IfItutCurrentStatsEntry": nndsxT1E1IfItutCurrentStatsEntry,
       "nndsxT1E1IfItutCurrentStatsUASState": nndsxT1E1IfItutCurrentStatsUASState,
       "nndsxT1E1IfItutCurrentStatsTimeInCurrent": nndsxT1E1IfItutCurrentStatsTimeInCurrent,
       "nndsxT1E1IfItutCurrentStatsES": nndsxT1E1IfItutCurrentStatsES,
       "nndsxT1E1IfItutCurrentStatsUAS": nndsxT1E1IfItutCurrentStatsUAS,
       "nndsxT1E1IfItutCurrentStatsBBE": nndsxT1E1IfItutCurrentStatsBBE,
       "nndsxT1E1IfItutCurrentStatsSES": nndsxT1E1IfItutCurrentStatsSES,
       "nndsxT1E1IfItutTotalStatsTable": nndsxT1E1IfItutTotalStatsTable,
       "nndsxT1E1IfItutTotalStatsEntry": nndsxT1E1IfItutTotalStatsEntry,
       "nndsxT1E1IfItutTotalStatsES": nndsxT1E1IfItutTotalStatsES,
       "nndsxT1E1IfItutTotalStatsUAS": nndsxT1E1IfItutTotalStatsUAS,
       "nndsxT1E1IfItutTotalStatsBBE": nndsxT1E1IfItutTotalStatsBBE,
       "nndsxT1E1IfItutTotalStatsSES": nndsxT1E1IfItutTotalStatsSES,
       "nndsxT1E1IfItutArchiveStatsTable": nndsxT1E1IfItutArchiveStatsTable,
       "nndsxT1E1IfItutArchiveStatsEntry": nndsxT1E1IfItutArchiveStatsEntry,
       "nndsxT1E1IfItutArchiveInterval": nndsxT1E1IfItutArchiveInterval,
       "nndsxT1E1IfItutArchiveStatsES": nndsxT1E1IfItutArchiveStatsES,
       "nndsxT1E1IfItutArchiveStatsUAS": nndsxT1E1IfItutArchiveStatsUAS,
       "nndsxT1E1IfItutArchiveStatsBBE": nndsxT1E1IfItutArchiveStatsBBE,
       "nndsxT1E1IfItutArchiveStatsSES": nndsxT1E1IfItutArchiveStatsSES,
       "nndsxT1E1IfIetfStatsGroup": nndsxT1E1IfIetfStatsGroup,
       "nndsxT1E1IfIetfCurrentStatsTable": nndsxT1E1IfIetfCurrentStatsTable,
       "nndsxT1E1IfIetfCurrentStatsEntry": nndsxT1E1IfIetfCurrentStatsEntry,
       "nndsxT1E1IfIetfCurrentStatsUASState": nndsxT1E1IfIetfCurrentStatsUASState,
       "nndsxT1E1IfIetfCurrentStatsTimeInCurrent": nndsxT1E1IfIetfCurrentStatsTimeInCurrent,
       "nndsxT1E1IfIetfCurrentStatsES": nndsxT1E1IfIetfCurrentStatsES,
       "nndsxT1E1IfIetfCurrentStatsSES": nndsxT1E1IfIetfCurrentStatsSES,
       "nndsxT1E1IfIetfCurrentStatsSEFS": nndsxT1E1IfIetfCurrentStatsSEFS,
       "nndsxT1E1IfIetfCurrentStatsUAS": nndsxT1E1IfIetfCurrentStatsUAS,
       "nndsxT1E1IfIetfCurrentStatsCSS": nndsxT1E1IfIetfCurrentStatsCSS,
       "nndsxT1E1IfIetfCurrentStatsPCV": nndsxT1E1IfIetfCurrentStatsPCV,
       "nndsxT1E1IfIetfCurrentStatsLES": nndsxT1E1IfIetfCurrentStatsLES,
       "nndsxT1E1IfIetfCurrentStatsBES": nndsxT1E1IfIetfCurrentStatsBES,
       "nndsxT1E1IfIetfCurrentStatsDM": nndsxT1E1IfIetfCurrentStatsDM,
       "nndsxT1E1IfIetfCurrentStatsLCV": nndsxT1E1IfIetfCurrentStatsLCV,
       "nndsxT1E1IfIetfTotalStatsTable": nndsxT1E1IfIetfTotalStatsTable,
       "nndsxT1E1IfIetfTotalStatsEntry": nndsxT1E1IfIetfTotalStatsEntry,
       "nndsxT1E1IfIetfTotalStatsES": nndsxT1E1IfIetfTotalStatsES,
       "nndsxT1E1IfIetfTotalStatsSES": nndsxT1E1IfIetfTotalStatsSES,
       "nndsxT1E1IfIetfTotalStatsSEFS": nndsxT1E1IfIetfTotalStatsSEFS,
       "nndsxT1E1IfIetfTotalStatsUAS": nndsxT1E1IfIetfTotalStatsUAS,
       "nndsxT1E1IfIetfTotalStatsCSS": nndsxT1E1IfIetfTotalStatsCSS,
       "nndsxT1E1IfIetfTotalStatsPCV": nndsxT1E1IfIetfTotalStatsPCV,
       "nndsxT1E1IfIetfTotalStatsLES": nndsxT1E1IfIetfTotalStatsLES,
       "nndsxT1E1IfIetfTotalStatsBES": nndsxT1E1IfIetfTotalStatsBES,
       "nndsxT1E1IfIetfTotalStatsDM": nndsxT1E1IfIetfTotalStatsDM,
       "nndsxT1E1IfIetfTotalStatsLCV": nndsxT1E1IfIetfTotalStatsLCV,
       "nndsxT1E1IfIetfArchiveStatsTable": nndsxT1E1IfIetfArchiveStatsTable,
       "nndsxT1E1IfIetfArchiveStatsEntry": nndsxT1E1IfIetfArchiveStatsEntry,
       "nndsxT1E1IfIetfArchiveStatsInterval": nndsxT1E1IfIetfArchiveStatsInterval,
       "nndsxT1E1IfIetfArchiveStatsES": nndsxT1E1IfIetfArchiveStatsES,
       "nndsxT1E1IfIetfArchiveStatsSES": nndsxT1E1IfIetfArchiveStatsSES,
       "nndsxT1E1IfIetfArchiveStatsSEFS": nndsxT1E1IfIetfArchiveStatsSEFS,
       "nndsxT1E1IfIetfArchiveStatsUAS": nndsxT1E1IfIetfArchiveStatsUAS,
       "nndsxT1E1IfIetfArchiveStatsCSS": nndsxT1E1IfIetfArchiveStatsCSS,
       "nndsxT1E1IfIetfArchiveStatsPCV": nndsxT1E1IfIetfArchiveStatsPCV,
       "nndsxT1E1IfIetfArchiveStatsLES": nndsxT1E1IfIetfArchiveStatsLES,
       "nndsxT1E1IfIetfArchiveStatsBES": nndsxT1E1IfIetfArchiveStatsBES,
       "nndsxT1E1IfIetfArchiveStatsDM": nndsxT1E1IfIetfArchiveStatsDM,
       "nndsxT1E1IfIetfArchiveStatsLCV": nndsxT1E1IfIetfArchiveStatsLCV,
       "nndsxT1E1IfUserStatsGroup": nndsxT1E1IfUserStatsGroup,
       "nndsxT1E1IfUserCurrentStatsTable": nndsxT1E1IfUserCurrentStatsTable,
       "nndsxT1E1IfUserCurrentStatsEntry": nndsxT1E1IfUserCurrentStatsEntry,
       "nndsxT1E1IfUserCurrentStatsUASState": nndsxT1E1IfUserCurrentStatsUASState,
       "nndsxT1E1IfUserCurrentStatsTimeInCurrent": nndsxT1E1IfUserCurrentStatsTimeInCurrent,
       "nndsxT1E1IfUserCurrentStatsEEV": nndsxT1E1IfUserCurrentStatsEEV,
       "nndsxT1E1IfUserCurrentStatsES": nndsxT1E1IfUserCurrentStatsES,
       "nndsxT1E1IfUserCurrentStatsUAS": nndsxT1E1IfUserCurrentStatsUAS,
       "nndsxT1E1IfUserCurrentStatsBES": nndsxT1E1IfUserCurrentStatsBES,
       "nndsxT1E1IfUserCurrentStatsSES": nndsxT1E1IfUserCurrentStatsSES,
       "nndsxT1E1IfUserCurrentStatsLOFC": nndsxT1E1IfUserCurrentStatsLOFC,
       "nndsxT1E1IfUserCurrentStatsCSS": nndsxT1E1IfUserCurrentStatsCSS,
       "nndsxT1E1IfUserCurrentStatsBPV": nndsxT1E1IfUserCurrentStatsBPV,
       "nndsxT1E1IfUserCurrentStatsOOF": nndsxT1E1IfUserCurrentStatsOOF,
       "nndsxT1E1IfUserCurrentStatsCRC": nndsxT1E1IfUserCurrentStatsCRC,
       "nndsxT1E1IfUserTotalStatsTable": nndsxT1E1IfUserTotalStatsTable,
       "nndsxT1E1IfUserTotalStatsEntry": nndsxT1E1IfUserTotalStatsEntry,
       "nndsxT1E1IfUserTotalStatsDay": nndsxT1E1IfUserTotalStatsDay,
       "nndsxT1E1IfUserTotalStatsEEV": nndsxT1E1IfUserTotalStatsEEV,
       "nndsxT1E1IfUserTotalStatsES": nndsxT1E1IfUserTotalStatsES,
       "nndsxT1E1IfUserTotalStatsUAS": nndsxT1E1IfUserTotalStatsUAS,
       "nndsxT1E1IfUserTotalStatsBES": nndsxT1E1IfUserTotalStatsBES,
       "nndsxT1E1IfUserTotalStatsSES": nndsxT1E1IfUserTotalStatsSES,
       "nndsxT1E1IfUserTotalStatsLOFC": nndsxT1E1IfUserTotalStatsLOFC,
       "nndsxT1E1IfUserTotalStatsCSS": nndsxT1E1IfUserTotalStatsCSS,
       "nndsxT1E1IfUserTotalStatsBPV": nndsxT1E1IfUserTotalStatsBPV,
       "nndsxT1E1IfUserTotalStatsOOF": nndsxT1E1IfUserTotalStatsOOF,
       "nndsxT1E1IfUserTotalStatsCRC": nndsxT1E1IfUserTotalStatsCRC,
       "nndsxT1E1IfUserLifetimeStatsTable": nndsxT1E1IfUserLifetimeStatsTable,
       "nndsxT1E1IfUserLifetimeStatsEntry": nndsxT1E1IfUserLifetimeStatsEntry,
       "nndsxT1E1IfUserLifetimeStatsEEV": nndsxT1E1IfUserLifetimeStatsEEV,
       "nndsxT1E1IfUserLifetimeStatsES": nndsxT1E1IfUserLifetimeStatsES,
       "nndsxT1E1IfUserLifetimeStatsUAS": nndsxT1E1IfUserLifetimeStatsUAS,
       "nndsxT1E1IfUserLifetimeStatsBES": nndsxT1E1IfUserLifetimeStatsBES,
       "nndsxT1E1IfUserLifetimeStatsSES": nndsxT1E1IfUserLifetimeStatsSES,
       "nndsxT1E1IfUserLifetimeStatsLOFC": nndsxT1E1IfUserLifetimeStatsLOFC,
       "nndsxT1E1IfUserLifetimeStatsCSS": nndsxT1E1IfUserLifetimeStatsCSS,
       "nndsxT1E1IfUserLifetimeStatsBPV": nndsxT1E1IfUserLifetimeStatsBPV,
       "nndsxT1E1IfUserLifetimeStatsOOF": nndsxT1E1IfUserLifetimeStatsOOF,
       "nndsxT1E1IfUserLifetimeStatsCRC": nndsxT1E1IfUserLifetimeStatsCRC,
       "nndsxT1E1IfUserArchiveStatsTable": nndsxT1E1IfUserArchiveStatsTable,
       "nndsxT1E1IfUserArchiveStatsEntry": nndsxT1E1IfUserArchiveStatsEntry,
       "nndsxT1E1IfUserArchiveStatsInterval": nndsxT1E1IfUserArchiveStatsInterval,
       "nndsxT1E1IfUserArchiveStatsEEV": nndsxT1E1IfUserArchiveStatsEEV,
       "nndsxT1E1IfUserArchiveStatsES": nndsxT1E1IfUserArchiveStatsES,
       "nndsxT1E1IfUserArchiveStatsUAS": nndsxT1E1IfUserArchiveStatsUAS,
       "nndsxT1E1IfUserArchiveStatsBES": nndsxT1E1IfUserArchiveStatsBES,
       "nndsxT1E1IfUserArchiveStatsSES": nndsxT1E1IfUserArchiveStatsSES,
       "nndsxT1E1IfUserArchiveStatsLOFC": nndsxT1E1IfUserArchiveStatsLOFC,
       "nndsxT1E1IfUserArchiveStatsCSS": nndsxT1E1IfUserArchiveStatsCSS,
       "nndsxT1E1IfUserArchiveStatsBPV": nndsxT1E1IfUserArchiveStatsBPV,
       "nndsxT1E1IfUserArchiveStatsOOF": nndsxT1E1IfUserArchiveStatsOOF,
       "nndsxT1E1IfUserArchiveStatsCRC": nndsxT1E1IfUserArchiveStatsCRC,
       "nndsxT1E1Traps": nndsxT1E1Traps,
       "nndsxT1E1Notifications": nndsxT1E1Notifications,
       "nndsxT1E1AlarmOnTrap": nndsxT1E1AlarmOnTrap,
       "nndsxT1E1AlarmOffTrap": nndsxT1E1AlarmOffTrap,
       "nndsxT1E1TrapVariables": nndsxT1E1TrapVariables,
       "nndsxT1E1Number": nndsxT1E1Number,
       "nndsxT1E1Type": nndsxT1E1Type,
       "nndsxT1E1T3Number": nndsxT1E1T3Number,
       "nndsxT1E1AlarmType": nndsxT1E1AlarmType,
       "nndsxT1E1NotificationGroup": nndsxT1E1NotificationGroup}
)
