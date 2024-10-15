# SNMP MIB module (TERAWAVE-teraEPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraEPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:15 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraEPSGroup_ObjectIdentity = ObjectIdentity
teraEPSGroup = _TeraEPSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 12)
)
_TeraLevel1EPSConfigTable_Object = MibTable
teraLevel1EPSConfigTable = _TeraLevel1EPSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1)
)
if mibBuilder.loadTexts:
    teraLevel1EPSConfigTable.setStatus("mandatory")
_TeraLevel1EPSConfigTableEntry_Object = MibTableRow
teraLevel1EPSConfigTableEntry = _TeraLevel1EPSConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1)
)
teraLevel1EPSConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraEPS-MIB", "teraLevel1ConfigIndex"),
)
if mibBuilder.loadTexts:
    teraLevel1EPSConfigTableEntry.setStatus("mandatory")


class _TeraLevel1ConfigIndex_Type(Integer32):
    """Custom type teraLevel1ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TeraLevel1ConfigIndex_Type.__name__ = "Integer32"
_TeraLevel1ConfigIndex_Object = MibTableColumn
teraLevel1ConfigIndex = _TeraLevel1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 1),
    _TeraLevel1ConfigIndex_Type()
)
teraLevel1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1ConfigIndex.setStatus("mandatory")


class _TeraLevel1ProtectingUnit_Type(Integer32):
    """Custom type teraLevel1ProtectingUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TeraLevel1ProtectingUnit_Type.__name__ = "Integer32"
_TeraLevel1ProtectingUnit_Object = MibTableColumn
teraLevel1ProtectingUnit = _TeraLevel1ProtectingUnit_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 2),
    _TeraLevel1ProtectingUnit_Type()
)
teraLevel1ProtectingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLevel1ProtectingUnit.setStatus("mandatory")


class _TeraLevel1AdminProtectSwitch_Type(Integer32):
    """Custom type teraLevel1AdminProtectSwitch based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("force-p2w", 7),
          ("force-w2p", 2),
          ("lock", 3),
          ("manual-p2w", 6),
          ("manual-w2p", 1),
          ("none", 0),
          ("not-used", 8),
          ("release", 4),
          ("unlock", 5))
    )


_TeraLevel1AdminProtectSwitch_Type.__name__ = "Integer32"
_TeraLevel1AdminProtectSwitch_Object = MibTableColumn
teraLevel1AdminProtectSwitch = _TeraLevel1AdminProtectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 3),
    _TeraLevel1AdminProtectSwitch_Type()
)
teraLevel1AdminProtectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLevel1AdminProtectSwitch.setStatus("mandatory")


class _TeraLevel1AdminProtectStatus_Type(Integer32):
    """Custom type teraLevel1AdminProtectStatus based on Integer32"""
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
          ("protection", 2),
          ("working", 1))
    )


_TeraLevel1AdminProtectStatus_Type.__name__ = "Integer32"
_TeraLevel1AdminProtectStatus_Object = MibTableColumn
teraLevel1AdminProtectStatus = _TeraLevel1AdminProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 4),
    _TeraLevel1AdminProtectStatus_Type()
)
teraLevel1AdminProtectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLevel1AdminProtectStatus.setStatus("mandatory")


class _TeraLevel1AdminProtectSwitchReason_Type(Integer32):
    """Custom type teraLevel1AdminProtectSwitchReason based on Integer32"""
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
        *(("auto", 4),
          ("forced", 1),
          ("locked", 2),
          ("manual", 3),
          ("none", 0))
    )


_TeraLevel1AdminProtectSwitchReason_Type.__name__ = "Integer32"
_TeraLevel1AdminProtectSwitchReason_Object = MibTableColumn
teraLevel1AdminProtectSwitchReason = _TeraLevel1AdminProtectSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 5),
    _TeraLevel1AdminProtectSwitchReason_Type()
)
teraLevel1AdminProtectSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1AdminProtectSwitchReason.setStatus("mandatory")


class _TeraLevel1ProtectSwitchState_Type(Integer32):
    """Custom type teraLevel1ProtectSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 1))
    )


_TeraLevel1ProtectSwitchState_Type.__name__ = "Integer32"
_TeraLevel1ProtectSwitchState_Object = MibTableColumn
teraLevel1ProtectSwitchState = _TeraLevel1ProtectSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 6),
    _TeraLevel1ProtectSwitchState_Type()
)
teraLevel1ProtectSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1ProtectSwitchState.setStatus("mandatory")
_TeraLevel1OperProtectSwitchReason_Type = Integer32
_TeraLevel1OperProtectSwitchReason_Object = MibTableColumn
teraLevel1OperProtectSwitchReason = _TeraLevel1OperProtectSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 7),
    _TeraLevel1OperProtectSwitchReason_Type()
)
teraLevel1OperProtectSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1OperProtectSwitchReason.setStatus("mandatory")
_TeraLevel1OperProtectSwitchSource_Type = Integer32
_TeraLevel1OperProtectSwitchSource_Object = MibTableColumn
teraLevel1OperProtectSwitchSource = _TeraLevel1OperProtectSwitchSource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 1, 1, 8),
    _TeraLevel1OperProtectSwitchSource_Type()
)
teraLevel1OperProtectSwitchSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1OperProtectSwitchSource.setStatus("mandatory")
_TeraLinkEPSConfigTable_Object = MibTable
teraLinkEPSConfigTable = _TeraLinkEPSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2)
)
if mibBuilder.loadTexts:
    teraLinkEPSConfigTable.setStatus("mandatory")
_TeraLinkEPSConfigTableEntry_Object = MibTableRow
teraLinkEPSConfigTableEntry = _TeraLinkEPSConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2, 1)
)
teraLinkEPSConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraEPS-MIB", "teraLevel1ConfigIndex"),
    (0, "TERAWAVE-teraEPS-MIB", "teraPonIndex"),
)
if mibBuilder.loadTexts:
    teraLinkEPSConfigTableEntry.setStatus("mandatory")


class _TeraLinkProtectingUnitLevel1Index_Type(Integer32):
    """Custom type teraLinkProtectingUnitLevel1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraLinkProtectingUnitLevel1Index_Type.__name__ = "Integer32"
_TeraLinkProtectingUnitLevel1Index_Object = MibTableColumn
teraLinkProtectingUnitLevel1Index = _TeraLinkProtectingUnitLevel1Index_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2, 1, 1),
    _TeraLinkProtectingUnitLevel1Index_Type()
)
teraLinkProtectingUnitLevel1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLinkProtectingUnitLevel1Index.setStatus("mandatory")


class _TeraLinkProtectingUnitPonIndex_Type(Integer32):
    """Custom type teraLinkProtectingUnitPonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 33),
    )


_TeraLinkProtectingUnitPonIndex_Type.__name__ = "Integer32"
_TeraLinkProtectingUnitPonIndex_Object = MibTableColumn
teraLinkProtectingUnitPonIndex = _TeraLinkProtectingUnitPonIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2, 1, 2),
    _TeraLinkProtectingUnitPonIndex_Type()
)
teraLinkProtectingUnitPonIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLinkProtectingUnitPonIndex.setStatus("mandatory")


class _TeraLinkAdminProtectSwitch_Type(Integer32):
    """Custom type teraLinkAdminProtectSwitch based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("force-p2w", 7),
          ("force-w2p", 2),
          ("lock", 3),
          ("manual-p2w", 6),
          ("manual-w2p", 1),
          ("none", 0),
          ("not-used", 8),
          ("release", 4),
          ("unlock", 5))
    )


_TeraLinkAdminProtectSwitch_Type.__name__ = "Integer32"
_TeraLinkAdminProtectSwitch_Object = MibTableColumn
teraLinkAdminProtectSwitch = _TeraLinkAdminProtectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2, 1, 3),
    _TeraLinkAdminProtectSwitch_Type()
)
teraLinkAdminProtectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLinkAdminProtectSwitch.setStatus("mandatory")


class _TeraLinkAdminProtectStatus_Type(Integer32):
    """Custom type teraLinkAdminProtectStatus based on Integer32"""
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
          ("protection", 2),
          ("working", 1))
    )


_TeraLinkAdminProtectStatus_Type.__name__ = "Integer32"
_TeraLinkAdminProtectStatus_Object = MibTableColumn
teraLinkAdminProtectStatus = _TeraLinkAdminProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2, 1, 4),
    _TeraLinkAdminProtectStatus_Type()
)
teraLinkAdminProtectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLinkAdminProtectStatus.setStatus("mandatory")


class _TeraLinkAdminProtectSwitchReason_Type(Integer32):
    """Custom type teraLinkAdminProtectSwitchReason based on Integer32"""
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
        *(("auto", 4),
          ("forced", 1),
          ("locked", 2),
          ("manual", 3),
          ("none", 0))
    )


_TeraLinkAdminProtectSwitchReason_Type.__name__ = "Integer32"
_TeraLinkAdminProtectSwitchReason_Object = MibTableColumn
teraLinkAdminProtectSwitchReason = _TeraLinkAdminProtectSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 2, 1, 5),
    _TeraLinkAdminProtectSwitchReason_Type()
)
teraLinkAdminProtectSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkAdminProtectSwitchReason.setStatus("mandatory")
_TeraLinkCardEPSConfigTable_Object = MibTable
teraLinkCardEPSConfigTable = _TeraLinkCardEPSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3)
)
if mibBuilder.loadTexts:
    teraLinkCardEPSConfigTable.setStatus("mandatory")
_TeraLinkCardEPSConfigTableEntry_Object = MibTableRow
teraLinkCardEPSConfigTableEntry = _TeraLinkCardEPSConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1)
)
teraLinkCardEPSConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraEPS-MIB", "teraLevel1ConfigIndex"),
    (0, "TERAWAVE-teraEPS-MIB", "teraPonIndex"),
    (0, "TERAWAVE-teraEPS-MIB", "teraNELevel2Slot"),
)
if mibBuilder.loadTexts:
    teraLinkCardEPSConfigTableEntry.setStatus("mandatory")


class _TeraLinkCardProtectingUnitLevel1Index_Type(Integer32):
    """Custom type teraLinkCardProtectingUnitLevel1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraLinkCardProtectingUnitLevel1Index_Type.__name__ = "Integer32"
_TeraLinkCardProtectingUnitLevel1Index_Object = MibTableColumn
teraLinkCardProtectingUnitLevel1Index = _TeraLinkCardProtectingUnitLevel1Index_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 1),
    _TeraLinkCardProtectingUnitLevel1Index_Type()
)
teraLinkCardProtectingUnitLevel1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardProtectingUnitLevel1Index.setStatus("mandatory")


class _TeraLinkCardProtectingUnitPonIndex_Type(Integer32):
    """Custom type teraLinkCardProtectingUnitPonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 33),
    )


_TeraLinkCardProtectingUnitPonIndex_Type.__name__ = "Integer32"
_TeraLinkCardProtectingUnitPonIndex_Object = MibTableColumn
teraLinkCardProtectingUnitPonIndex = _TeraLinkCardProtectingUnitPonIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 2),
    _TeraLinkCardProtectingUnitPonIndex_Type()
)
teraLinkCardProtectingUnitPonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardProtectingUnitPonIndex.setStatus("mandatory")


class _TeraLinkCardProtectingUnitLevel2Index_Type(Integer32):
    """Custom type teraLinkCardProtectingUnitLevel2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraLinkCardProtectingUnitLevel2Index_Type.__name__ = "Integer32"
_TeraLinkCardProtectingUnitLevel2Index_Object = MibTableColumn
teraLinkCardProtectingUnitLevel2Index = _TeraLinkCardProtectingUnitLevel2Index_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 3),
    _TeraLinkCardProtectingUnitLevel2Index_Type()
)
teraLinkCardProtectingUnitLevel2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardProtectingUnitLevel2Index.setStatus("mandatory")


class _TeraLinkCardAdminProtectSwitch_Type(Integer32):
    """Custom type teraLinkCardAdminProtectSwitch based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("force-p2w", 7),
          ("force-w2p", 2),
          ("lock", 3),
          ("manual-p2w", 6),
          ("manual-w2p", 1),
          ("none", 0),
          ("not-used", 8),
          ("release", 4),
          ("unlock", 5))
    )


_TeraLinkCardAdminProtectSwitch_Type.__name__ = "Integer32"
_TeraLinkCardAdminProtectSwitch_Object = MibTableColumn
teraLinkCardAdminProtectSwitch = _TeraLinkCardAdminProtectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 4),
    _TeraLinkCardAdminProtectSwitch_Type()
)
teraLinkCardAdminProtectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLinkCardAdminProtectSwitch.setStatus("mandatory")


class _TeraLinkCardAdminProtectSwitchReason_Type(Integer32):
    """Custom type teraLinkCardAdminProtectSwitchReason based on Integer32"""
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
        *(("auto", 4),
          ("forced", 1),
          ("locked", 2),
          ("manual", 3),
          ("none", 0))
    )


_TeraLinkCardAdminProtectSwitchReason_Type.__name__ = "Integer32"
_TeraLinkCardAdminProtectSwitchReason_Object = MibTableColumn
teraLinkCardAdminProtectSwitchReason = _TeraLinkCardAdminProtectSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 5),
    _TeraLinkCardAdminProtectSwitchReason_Type()
)
teraLinkCardAdminProtectSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardAdminProtectSwitchReason.setStatus("mandatory")


class _TeraLinkCardProtectSwitchState_Type(Integer32):
    """Custom type teraLinkCardProtectSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 1))
    )


_TeraLinkCardProtectSwitchState_Type.__name__ = "Integer32"
_TeraLinkCardProtectSwitchState_Object = MibTableColumn
teraLinkCardProtectSwitchState = _TeraLinkCardProtectSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 6),
    _TeraLinkCardProtectSwitchState_Type()
)
teraLinkCardProtectSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardProtectSwitchState.setStatus("mandatory")
_TeraLinkCardOperProtectSwitchReason_Type = Integer32
_TeraLinkCardOperProtectSwitchReason_Object = MibTableColumn
teraLinkCardOperProtectSwitchReason = _TeraLinkCardOperProtectSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 7),
    _TeraLinkCardOperProtectSwitchReason_Type()
)
teraLinkCardOperProtectSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardOperProtectSwitchReason.setStatus("mandatory")
_TeraLinkCardOperProtectSwitchSource_Type = Integer32
_TeraLinkCardOperProtectSwitchSource_Object = MibTableColumn
teraLinkCardOperProtectSwitchSource = _TeraLinkCardOperProtectSwitchSource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 8),
    _TeraLinkCardOperProtectSwitchSource_Type()
)
teraLinkCardOperProtectSwitchSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardOperProtectSwitchSource.setStatus("mandatory")


class _TeraLinkCardAdminProtectStatus_Type(Integer32):
    """Custom type teraLinkCardAdminProtectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection", 2),
          ("working", 1))
    )


_TeraLinkCardAdminProtectStatus_Type.__name__ = "Integer32"
_TeraLinkCardAdminProtectStatus_Object = MibTableColumn
teraLinkCardAdminProtectStatus = _TeraLinkCardAdminProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 12, 3, 1, 9),
    _TeraLinkCardAdminProtectStatus_Type()
)
teraLinkCardAdminProtectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLinkCardAdminProtectStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraEPS-MIB",
    **{"terawave": terawave,
       "teraEPSGroup": teraEPSGroup,
       "teraLevel1EPSConfigTable": teraLevel1EPSConfigTable,
       "teraLevel1EPSConfigTableEntry": teraLevel1EPSConfigTableEntry,
       "teraLevel1ConfigIndex": teraLevel1ConfigIndex,
       "teraLevel1ProtectingUnit": teraLevel1ProtectingUnit,
       "teraLevel1AdminProtectSwitch": teraLevel1AdminProtectSwitch,
       "teraLevel1AdminProtectStatus": teraLevel1AdminProtectStatus,
       "teraLevel1AdminProtectSwitchReason": teraLevel1AdminProtectSwitchReason,
       "teraLevel1ProtectSwitchState": teraLevel1ProtectSwitchState,
       "teraLevel1OperProtectSwitchReason": teraLevel1OperProtectSwitchReason,
       "teraLevel1OperProtectSwitchSource": teraLevel1OperProtectSwitchSource,
       "teraLinkEPSConfigTable": teraLinkEPSConfigTable,
       "teraLinkEPSConfigTableEntry": teraLinkEPSConfigTableEntry,
       "teraLinkProtectingUnitLevel1Index": teraLinkProtectingUnitLevel1Index,
       "teraLinkProtectingUnitPonIndex": teraLinkProtectingUnitPonIndex,
       "teraLinkAdminProtectSwitch": teraLinkAdminProtectSwitch,
       "teraLinkAdminProtectStatus": teraLinkAdminProtectStatus,
       "teraLinkAdminProtectSwitchReason": teraLinkAdminProtectSwitchReason,
       "teraLinkCardEPSConfigTable": teraLinkCardEPSConfigTable,
       "teraLinkCardEPSConfigTableEntry": teraLinkCardEPSConfigTableEntry,
       "teraLinkCardProtectingUnitLevel1Index": teraLinkCardProtectingUnitLevel1Index,
       "teraLinkCardProtectingUnitPonIndex": teraLinkCardProtectingUnitPonIndex,
       "teraLinkCardProtectingUnitLevel2Index": teraLinkCardProtectingUnitLevel2Index,
       "teraLinkCardAdminProtectSwitch": teraLinkCardAdminProtectSwitch,
       "teraLinkCardAdminProtectSwitchReason": teraLinkCardAdminProtectSwitchReason,
       "teraLinkCardProtectSwitchState": teraLinkCardProtectSwitchState,
       "teraLinkCardOperProtectSwitchReason": teraLinkCardOperProtectSwitchReason,
       "teraLinkCardOperProtectSwitchSource": teraLinkCardOperProtectSwitchSource,
       "teraLinkCardAdminProtectStatus": teraLinkCardAdminProtectStatus}
)
