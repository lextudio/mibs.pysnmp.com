# SNMP MIB module (Novell-LANalyzer-Ext-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Novell-LANalyzer-Ext-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:25 2024
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

(EntryStatus,
 OwnerString,
 alarmFallingThreshold,
 alarmIndex,
 alarmRisingThreshold,
 alarmSampleType,
 alarmValue,
 alarmVariable,
 channelDescription,
 channelIndex,
 channelMatches,
 rmon) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "EntryStatus",
    "OwnerString",
    "alarmFallingThreshold",
    "alarmIndex",
    "alarmRisingThreshold",
    "alarmSampleType",
    "alarmValue",
    "alarmVariable",
    "channelDescription",
    "channelIndex",
    "channelMatches",
    "rmon")

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
    "NotificationType",
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_ProductType_ObjectIdentity = ObjectIdentity
productType = _ProductType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1)
)
_Lantern_ObjectIdentity = ObjectIdentity
lantern = _Lantern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 1)
)
_Lantern_rmonPlus_ObjectIdentity = ObjectIdentity
lantern_rmonPlus = _Lantern_rmonPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 1, 3)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_RmonPlus_mib_ObjectIdentity = ObjectIdentity
rmonPlus_mib = _RmonPlus_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13)
)
_RmonShadow_ObjectIdentity = ObjectIdentity
rmonShadow = _RmonShadow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1)
)
_RpAlarm_ObjectIdentity = ObjectIdentity
rpAlarm = _RpAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 3)
)
_RpAlarmTable_Object = MibTable
rpAlarmTable = _RpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rpAlarmTable.setStatus("mandatory")
_RpAlarmEntry_Object = MibTableRow
rpAlarmEntry = _RpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 3, 1, 1)
)
rpAlarmEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpAlarmIndex"),
)
if mibBuilder.loadTexts:
    rpAlarmEntry.setStatus("mandatory")


class _RpAlarmIndex_Type(Integer32):
    """Custom type rpAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpAlarmIndex_Type.__name__ = "Integer32"
_RpAlarmIndex_Object = MibTableColumn
rpAlarmIndex = _RpAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 3, 1, 1, 1),
    _RpAlarmIndex_Type()
)
rpAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpAlarmIndex.setStatus("mandatory")


class _RpAlarmRisingDescription_Type(DisplayString):
    """Custom type rpAlarmRisingDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RpAlarmRisingDescription_Type.__name__ = "DisplayString"
_RpAlarmRisingDescription_Object = MibTableColumn
rpAlarmRisingDescription = _RpAlarmRisingDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 3, 1, 1, 2),
    _RpAlarmRisingDescription_Type()
)
rpAlarmRisingDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpAlarmRisingDescription.setStatus("mandatory")


class _RpAlarmFallingDescription_Type(DisplayString):
    """Custom type rpAlarmFallingDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RpAlarmFallingDescription_Type.__name__ = "DisplayString"
_RpAlarmFallingDescription_Object = MibTableColumn
rpAlarmFallingDescription = _RpAlarmFallingDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 3, 1, 1, 3),
    _RpAlarmFallingDescription_Type()
)
rpAlarmFallingDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpAlarmFallingDescription.setStatus("mandatory")
_RpHosts_ObjectIdentity = ObjectIdentity
rpHosts = _RpHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4)
)
_RpHostTable_Object = MibTable
rpHostTable = _RpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rpHostTable.setStatus("mandatory")
_RpHostEntry_Object = MibTableRow
rpHostEntry = _RpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1)
)
rpHostEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostIndex"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostAddress"),
)
if mibBuilder.loadTexts:
    rpHostEntry.setStatus("mandatory")
_RpHostAddress_Type = OctetString
_RpHostAddress_Object = MibTableColumn
rpHostAddress = _RpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1, 1),
    _RpHostAddress_Type()
)
rpHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostAddress.setStatus("mandatory")


class _RpHostCreationOrder_Type(Integer32):
    """Custom type rpHostCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostCreationOrder_Type.__name__ = "Integer32"
_RpHostCreationOrder_Object = MibTableColumn
rpHostCreationOrder = _RpHostCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1, 2),
    _RpHostCreationOrder_Type()
)
rpHostCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostCreationOrder.setStatus("mandatory")


class _RpHostIndex_Type(Integer32):
    """Custom type rpHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostIndex_Type.__name__ = "Integer32"
_RpHostIndex_Object = MibTableColumn
rpHostIndex = _RpHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1, 3),
    _RpHostIndex_Type()
)
rpHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostIndex.setStatus("mandatory")
_RpHostProtocols_Type = Integer32
_RpHostProtocols_Object = MibTableColumn
rpHostProtocols = _RpHostProtocols_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1, 4),
    _RpHostProtocols_Type()
)
rpHostProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostProtocols.setStatus("mandatory")


class _RpHostFirstTransmit_Type(TimeTicks):
    """Custom type rpHostFirstTransmit based on TimeTicks"""
    defaultValue = 0


_RpHostFirstTransmit_Object = MibTableColumn
rpHostFirstTransmit = _RpHostFirstTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1, 5),
    _RpHostFirstTransmit_Type()
)
rpHostFirstTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostFirstTransmit.setStatus("mandatory")


class _RpHostLastTransmit_Type(TimeTicks):
    """Custom type rpHostLastTransmit based on TimeTicks"""
    defaultValue = 0


_RpHostLastTransmit_Object = MibTableColumn
rpHostLastTransmit = _RpHostLastTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 2, 1, 6),
    _RpHostLastTransmit_Type()
)
rpHostLastTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostLastTransmit.setStatus("mandatory")
_RpHostTimeTable_Object = MibTable
rpHostTimeTable = _RpHostTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3)
)
if mibBuilder.loadTexts:
    rpHostTimeTable.setStatus("mandatory")
_RpHostTimeEntry_Object = MibTableRow
rpHostTimeEntry = _RpHostTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1)
)
rpHostTimeEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostTimeIndex"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    rpHostTimeEntry.setStatus("mandatory")
_RpHostTimeAddress_Type = OctetString
_RpHostTimeAddress_Object = MibTableColumn
rpHostTimeAddress = _RpHostTimeAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1, 1),
    _RpHostTimeAddress_Type()
)
rpHostTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostTimeAddress.setStatus("mandatory")


class _RpHostTimeCreationOrder_Type(Integer32):
    """Custom type rpHostTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostTimeCreationOrder_Type.__name__ = "Integer32"
_RpHostTimeCreationOrder_Object = MibTableColumn
rpHostTimeCreationOrder = _RpHostTimeCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1, 2),
    _RpHostTimeCreationOrder_Type()
)
rpHostTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostTimeCreationOrder.setStatus("mandatory")


class _RpHostTimeIndex_Type(Integer32):
    """Custom type rpHostTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostTimeIndex_Type.__name__ = "Integer32"
_RpHostTimeIndex_Object = MibTableColumn
rpHostTimeIndex = _RpHostTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1, 3),
    _RpHostTimeIndex_Type()
)
rpHostTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostTimeIndex.setStatus("mandatory")
_RpHostTimeProtocols_Type = Integer32
_RpHostTimeProtocols_Object = MibTableColumn
rpHostTimeProtocols = _RpHostTimeProtocols_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1, 4),
    _RpHostTimeProtocols_Type()
)
rpHostTimeProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostTimeProtocols.setStatus("mandatory")


class _RpHostTimeFirstTransmit_Type(TimeTicks):
    """Custom type rpHostTimeFirstTransmit based on TimeTicks"""
    defaultValue = 0


_RpHostTimeFirstTransmit_Object = MibTableColumn
rpHostTimeFirstTransmit = _RpHostTimeFirstTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1, 5),
    _RpHostTimeFirstTransmit_Type()
)
rpHostTimeFirstTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostTimeFirstTransmit.setStatus("mandatory")


class _RpHostTimeLastTransmit_Type(TimeTicks):
    """Custom type rpHostTimeLastTransmit based on TimeTicks"""
    defaultValue = 0


_RpHostTimeLastTransmit_Object = MibTableColumn
rpHostTimeLastTransmit = _RpHostTimeLastTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 4, 3, 1, 6),
    _RpHostTimeLastTransmit_Type()
)
rpHostTimeLastTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostTimeLastTransmit.setStatus("mandatory")
_RpMatrix_ObjectIdentity = ObjectIdentity
rpMatrix = _RpMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6)
)
_RpMatrixSDTable_Object = MibTable
rpMatrixSDTable = _RpMatrixSDTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2)
)
if mibBuilder.loadTexts:
    rpMatrixSDTable.setStatus("mandatory")
_RpMatrixSDEntry_Object = MibTableRow
rpMatrixSDEntry = _RpMatrixSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1)
)
rpMatrixSDEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpMatrixSDIndex"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpMatrixSDSourceAddress"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpMatrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    rpMatrixSDEntry.setStatus("mandatory")
_RpMatrixSDSourceAddress_Type = OctetString
_RpMatrixSDSourceAddress_Object = MibTableColumn
rpMatrixSDSourceAddress = _RpMatrixSDSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1, 1),
    _RpMatrixSDSourceAddress_Type()
)
rpMatrixSDSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixSDSourceAddress.setStatus("mandatory")
_RpMatrixSDDestAddress_Type = OctetString
_RpMatrixSDDestAddress_Object = MibTableColumn
rpMatrixSDDestAddress = _RpMatrixSDDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1, 2),
    _RpMatrixSDDestAddress_Type()
)
rpMatrixSDDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixSDDestAddress.setStatus("mandatory")


class _RpMatrixSDIndex_Type(Integer32):
    """Custom type rpMatrixSDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpMatrixSDIndex_Type.__name__ = "Integer32"
_RpMatrixSDIndex_Object = MibTableColumn
rpMatrixSDIndex = _RpMatrixSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1, 3),
    _RpMatrixSDIndex_Type()
)
rpMatrixSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixSDIndex.setStatus("mandatory")
_RpMatrixSDProtocols_Type = Integer32
_RpMatrixSDProtocols_Object = MibTableColumn
rpMatrixSDProtocols = _RpMatrixSDProtocols_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1, 4),
    _RpMatrixSDProtocols_Type()
)
rpMatrixSDProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixSDProtocols.setStatus("mandatory")
_RpMatrixSDFirstTransmit_Type = TimeTicks
_RpMatrixSDFirstTransmit_Object = MibTableColumn
rpMatrixSDFirstTransmit = _RpMatrixSDFirstTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1, 5),
    _RpMatrixSDFirstTransmit_Type()
)
rpMatrixSDFirstTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixSDFirstTransmit.setStatus("mandatory")
_RpMatrixSDLastTransmit_Type = TimeTicks
_RpMatrixSDLastTransmit_Object = MibTableColumn
rpMatrixSDLastTransmit = _RpMatrixSDLastTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 2, 1, 6),
    _RpMatrixSDLastTransmit_Type()
)
rpMatrixSDLastTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixSDLastTransmit.setStatus("mandatory")
_RpMatrixDSTable_Object = MibTable
rpMatrixDSTable = _RpMatrixDSTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3)
)
if mibBuilder.loadTexts:
    rpMatrixDSTable.setStatus("mandatory")
_RpMatrixDSEntry_Object = MibTableRow
rpMatrixDSEntry = _RpMatrixDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1)
)
rpMatrixDSEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpMatrixDSIndex"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpMatrixDSDestAddress"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpMatrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    rpMatrixDSEntry.setStatus("mandatory")
_RpMatrixDSSourceAddress_Type = OctetString
_RpMatrixDSSourceAddress_Object = MibTableColumn
rpMatrixDSSourceAddress = _RpMatrixDSSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1, 1),
    _RpMatrixDSSourceAddress_Type()
)
rpMatrixDSSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixDSSourceAddress.setStatus("mandatory")
_RpMatrixDSDestAddress_Type = OctetString
_RpMatrixDSDestAddress_Object = MibTableColumn
rpMatrixDSDestAddress = _RpMatrixDSDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1, 2),
    _RpMatrixDSDestAddress_Type()
)
rpMatrixDSDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixDSDestAddress.setStatus("mandatory")


class _RpMatrixDSIndex_Type(Integer32):
    """Custom type rpMatrixDSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpMatrixDSIndex_Type.__name__ = "Integer32"
_RpMatrixDSIndex_Object = MibTableColumn
rpMatrixDSIndex = _RpMatrixDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1, 3),
    _RpMatrixDSIndex_Type()
)
rpMatrixDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixDSIndex.setStatus("mandatory")
_RpMatrixDSProtocols_Type = Integer32
_RpMatrixDSProtocols_Object = MibTableColumn
rpMatrixDSProtocols = _RpMatrixDSProtocols_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1, 4),
    _RpMatrixDSProtocols_Type()
)
rpMatrixDSProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixDSProtocols.setStatus("mandatory")
_RpMatrixDSFirstTransmit_Type = TimeTicks
_RpMatrixDSFirstTransmit_Object = MibTableColumn
rpMatrixDSFirstTransmit = _RpMatrixDSFirstTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1, 5),
    _RpMatrixDSFirstTransmit_Type()
)
rpMatrixDSFirstTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixDSFirstTransmit.setStatus("mandatory")
_RpMatrixDSLastTransmit_Type = TimeTicks
_RpMatrixDSLastTransmit_Object = MibTableColumn
rpMatrixDSLastTransmit = _RpMatrixDSLastTransmit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 6, 3, 1, 6),
    _RpMatrixDSLastTransmit_Type()
)
rpMatrixDSLastTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMatrixDSLastTransmit.setStatus("mandatory")
_RpFilter_ObjectIdentity = ObjectIdentity
rpFilter = _RpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7)
)
_RpFilterTable_Object = MibTable
rpFilterTable = _RpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 1)
)
if mibBuilder.loadTexts:
    rpFilterTable.setStatus("mandatory")
_RpFilterEntry_Object = MibTableRow
rpFilterEntry = _RpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 1, 1)
)
rpFilterEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpFilterIndex"),
)
if mibBuilder.loadTexts:
    rpFilterEntry.setStatus("mandatory")


class _RpFilterIndex_Type(Integer32):
    """Custom type rpFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpFilterIndex_Type.__name__ = "Integer32"
_RpFilterIndex_Object = MibTableColumn
rpFilterIndex = _RpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 1, 1, 1),
    _RpFilterIndex_Type()
)
rpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpFilterIndex.setStatus("mandatory")


class _RpFilterProtocols_Type(Integer32):
    """Custom type rpFilterProtocols based on Integer32"""
    defaultValue = -1


_RpFilterProtocols_Object = MibTableColumn
rpFilterProtocols = _RpFilterProtocols_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 1, 1, 2),
    _RpFilterProtocols_Type()
)
rpFilterProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpFilterProtocols.setStatus("mandatory")
_RpChannelTable_Object = MibTable
rpChannelTable = _RpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 2)
)
if mibBuilder.loadTexts:
    rpChannelTable.setStatus("mandatory")
_RpChannelEntry_Object = MibTableRow
rpChannelEntry = _RpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 2, 1)
)
rpChannelEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpChannelIndex"),
)
if mibBuilder.loadTexts:
    rpChannelEntry.setStatus("mandatory")


class _RpChannelIndex_Type(Integer32):
    """Custom type rpChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpChannelIndex_Type.__name__ = "Integer32"
_RpChannelIndex_Object = MibTableColumn
rpChannelIndex = _RpChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 2, 1, 1),
    _RpChannelIndex_Type()
)
rpChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpChannelIndex.setStatus("mandatory")
_RpChannelMatchOctets_Type = Counter32
_RpChannelMatchOctets_Object = MibTableColumn
rpChannelMatchOctets = _RpChannelMatchOctets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 2, 1, 2),
    _RpChannelMatchOctets_Type()
)
rpChannelMatchOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpChannelMatchOctets.setStatus("mandatory")


class _RpChannelControlBufferFull_Type(Integer32):
    """Custom type rpChannelControlBufferFull based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RpChannelControlBufferFull_Type.__name__ = "Integer32"
_RpChannelControlBufferFull_Object = MibTableColumn
rpChannelControlBufferFull = _RpChannelControlBufferFull_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 7, 2, 1, 3),
    _RpChannelControlBufferFull_Type()
)
rpChannelControlBufferFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpChannelControlBufferFull.setStatus("mandatory")
_RpBuffer_ObjectIdentity = ObjectIdentity
rpBuffer = _RpBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 8)
)
_RpBufferControlTable_Object = MibTable
rpBufferControlTable = _RpBufferControlTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 8, 1)
)
if mibBuilder.loadTexts:
    rpBufferControlTable.setStatus("mandatory")
_RpBufferControlEntry_Object = MibTableRow
rpBufferControlEntry = _RpBufferControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 8, 1, 1)
)
rpBufferControlEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpBufferControlIndex"),
)
if mibBuilder.loadTexts:
    rpBufferControlEntry.setStatus("mandatory")


class _RpBufferControlIndex_Type(Integer32):
    """Custom type rpBufferControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpBufferControlIndex_Type.__name__ = "Integer32"
_RpBufferControlIndex_Object = MibTableColumn
rpBufferControlIndex = _RpBufferControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 8, 1, 1, 1),
    _RpBufferControlIndex_Type()
)
rpBufferControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpBufferControlIndex.setStatus("mandatory")
_RpBufferCaptureOctets_Type = Integer32
_RpBufferCaptureOctets_Object = MibTableColumn
rpBufferCaptureOctets = _RpBufferCaptureOctets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 1, 8, 1, 1, 2),
    _RpBufferCaptureOctets_Type()
)
rpBufferCaptureOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpBufferCaptureOctets.setStatus("mandatory")
_RmonExtensions_ObjectIdentity = ObjectIdentity
rmonExtensions = _RmonExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2)
)
_RpAdmin_ObjectIdentity = ObjectIdentity
rpAdmin = _RpAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 1)
)
_RpAdminSerialNumber_Type = OctetString
_RpAdminSerialNumber_Object = MibScalar
rpAdminSerialNumber = _RpAdminSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 1, 1),
    _RpAdminSerialNumber_Type()
)
rpAdminSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpAdminSerialNumber.setStatus("mandatory")


class _RpAdminProbeCopies_Type(Integer32):
    """Custom type rpAdminProbeCopies based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpAdminProbeCopies_Type.__name__ = "Integer32"
_RpAdminProbeCopies_Object = MibScalar
rpAdminProbeCopies = _RpAdminProbeCopies_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 1, 2),
    _RpAdminProbeCopies_Type()
)
rpAdminProbeCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpAdminProbeCopies.setStatus("mandatory")
_RpHostMonitor_ObjectIdentity = ObjectIdentity
rpHostMonitor = _RpHostMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2)
)
_RpHostMonitorControlTable_Object = MibTable
rpHostMonitorControlTable = _RpHostMonitorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rpHostMonitorControlTable.setStatus("mandatory")
_RpHostMonitorControlEntry_Object = MibTableRow
rpHostMonitorControlEntry = _RpHostMonitorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1)
)
rpHostMonitorControlEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostMonitorControlIndex"),
)
if mibBuilder.loadTexts:
    rpHostMonitorControlEntry.setStatus("mandatory")


class _RpHostMonitorControlIndex_Type(Integer32):
    """Custom type rpHostMonitorControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostMonitorControlIndex_Type.__name__ = "Integer32"
_RpHostMonitorControlIndex_Object = MibTableColumn
rpHostMonitorControlIndex = _RpHostMonitorControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 1),
    _RpHostMonitorControlIndex_Type()
)
rpHostMonitorControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostMonitorControlIndex.setStatus("mandatory")


class _RpHostMonitorControlHostIndex_Type(Integer32):
    """Custom type rpHostMonitorControlHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostMonitorControlHostIndex_Type.__name__ = "Integer32"
_RpHostMonitorControlHostIndex_Object = MibTableColumn
rpHostMonitorControlHostIndex = _RpHostMonitorControlHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 2),
    _RpHostMonitorControlHostIndex_Type()
)
rpHostMonitorControlHostIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorControlHostIndex.setStatus("mandatory")


class _RpHostMonitorControlActiveEvent_Type(Integer32):
    """Custom type rpHostMonitorControlActiveEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpHostMonitorControlActiveEvent_Type.__name__ = "Integer32"
_RpHostMonitorControlActiveEvent_Object = MibTableColumn
rpHostMonitorControlActiveEvent = _RpHostMonitorControlActiveEvent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 3),
    _RpHostMonitorControlActiveEvent_Type()
)
rpHostMonitorControlActiveEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorControlActiveEvent.setStatus("mandatory")


class _RpHostMonitorControlInactiveEvent_Type(Integer32):
    """Custom type rpHostMonitorControlInactiveEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpHostMonitorControlInactiveEvent_Type.__name__ = "Integer32"
_RpHostMonitorControlInactiveEvent_Object = MibTableColumn
rpHostMonitorControlInactiveEvent = _RpHostMonitorControlInactiveEvent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 4),
    _RpHostMonitorControlInactiveEvent_Type()
)
rpHostMonitorControlInactiveEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorControlInactiveEvent.setStatus("mandatory")


class _RpHostMonitorControlTimeout_Type(Integer32):
    """Custom type rpHostMonitorControlTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_RpHostMonitorControlTimeout_Type.__name__ = "Integer32"
_RpHostMonitorControlTimeout_Object = MibTableColumn
rpHostMonitorControlTimeout = _RpHostMonitorControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 5),
    _RpHostMonitorControlTimeout_Type()
)
rpHostMonitorControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorControlTimeout.setStatus("mandatory")
_RpHostMonitorControlOwner_Type = OwnerString
_RpHostMonitorControlOwner_Object = MibTableColumn
rpHostMonitorControlOwner = _RpHostMonitorControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 6),
    _RpHostMonitorControlOwner_Type()
)
rpHostMonitorControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorControlOwner.setStatus("mandatory")
_RpHostMonitorControlStatus_Type = EntryStatus
_RpHostMonitorControlStatus_Object = MibTableColumn
rpHostMonitorControlStatus = _RpHostMonitorControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 1, 1, 7),
    _RpHostMonitorControlStatus_Type()
)
rpHostMonitorControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorControlStatus.setStatus("mandatory")
_RpHostMonitorTable_Object = MibTable
rpHostMonitorTable = _RpHostMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rpHostMonitorTable.setStatus("mandatory")
_RpHostMonitorEntry_Object = MibTableRow
rpHostMonitorEntry = _RpHostMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 2, 1)
)
rpHostMonitorEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostMonitorIndex"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpHostMonitorAddress"),
)
if mibBuilder.loadTexts:
    rpHostMonitorEntry.setStatus("mandatory")


class _RpHostMonitorIndex_Type(Integer32):
    """Custom type rpHostMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpHostMonitorIndex_Type.__name__ = "Integer32"
_RpHostMonitorIndex_Object = MibTableColumn
rpHostMonitorIndex = _RpHostMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 2, 1, 1),
    _RpHostMonitorIndex_Type()
)
rpHostMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostMonitorIndex.setStatus("mandatory")
_RpHostMonitorAddress_Type = OctetString
_RpHostMonitorAddress_Object = MibTableColumn
rpHostMonitorAddress = _RpHostMonitorAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 2, 1, 2),
    _RpHostMonitorAddress_Type()
)
rpHostMonitorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostMonitorAddress.setStatus("mandatory")


class _RpHostMonitorActivity_Type(Integer32):
    """Custom type rpHostMonitorActivity based on Integer32"""
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


_RpHostMonitorActivity_Type.__name__ = "Integer32"
_RpHostMonitorActivity_Object = MibTableColumn
rpHostMonitorActivity = _RpHostMonitorActivity_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 2, 1, 3),
    _RpHostMonitorActivity_Type()
)
rpHostMonitorActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpHostMonitorActivity.setStatus("mandatory")


class _RpHostMonitorAddDelete_Type(Integer32):
    """Custom type rpHostMonitorAddDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_RpHostMonitorAddDelete_Type.__name__ = "Integer32"
_RpHostMonitorAddDelete_Object = MibTableColumn
rpHostMonitorAddDelete = _RpHostMonitorAddDelete_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 2, 2, 1, 4),
    _RpHostMonitorAddDelete_Type()
)
rpHostMonitorAddDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpHostMonitorAddDelete.setStatus("mandatory")
_RpDuplicateIp_ObjectIdentity = ObjectIdentity
rpDuplicateIp = _RpDuplicateIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3)
)
_RpDuplicateIpTable_Object = MibTable
rpDuplicateIpTable = _RpDuplicateIpTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rpDuplicateIpTable.setStatus("mandatory")
_RpDuplicateIpEntry_Object = MibTableRow
rpDuplicateIpEntry = _RpDuplicateIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3, 1, 1)
)
rpDuplicateIpEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpDuplicateIpAddress"),
)
if mibBuilder.loadTexts:
    rpDuplicateIpEntry.setStatus("mandatory")
_RpDuplicateIpAddress_Type = IpAddress
_RpDuplicateIpAddress_Object = MibTableColumn
rpDuplicateIpAddress = _RpDuplicateIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3, 1, 1, 1),
    _RpDuplicateIpAddress_Type()
)
rpDuplicateIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpDuplicateIpAddress.setStatus("mandatory")
_RpDuplicateIpNewMAC_Type = OctetString
_RpDuplicateIpNewMAC_Object = MibTableColumn
rpDuplicateIpNewMAC = _RpDuplicateIpNewMAC_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3, 1, 1, 2),
    _RpDuplicateIpNewMAC_Type()
)
rpDuplicateIpNewMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpDuplicateIpNewMAC.setStatus("mandatory")
_RpDuplicateIpOldMAC_Type = OctetString
_RpDuplicateIpOldMAC_Object = MibTableColumn
rpDuplicateIpOldMAC = _RpDuplicateIpOldMAC_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3, 1, 1, 3),
    _RpDuplicateIpOldMAC_Type()
)
rpDuplicateIpOldMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpDuplicateIpOldMAC.setStatus("mandatory")
_RpDuplicateIpTimestamp_Type = TimeTicks
_RpDuplicateIpTimestamp_Object = MibTableColumn
rpDuplicateIpTimestamp = _RpDuplicateIpTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 3, 1, 1, 4),
    _RpDuplicateIpTimestamp_Type()
)
rpDuplicateIpTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpDuplicateIpTimestamp.setStatus("mandatory")
_RpMacToIp_ObjectIdentity = ObjectIdentity
rpMacToIp = _RpMacToIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 4)
)
_RpMacToIpTable_Object = MibTable
rpMacToIpTable = _RpMacToIpTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 4, 1)
)
if mibBuilder.loadTexts:
    rpMacToIpTable.setStatus("mandatory")
_RpMacToIpEntry_Object = MibTableRow
rpMacToIpEntry = _RpMacToIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 4, 1, 1)
)
rpMacToIpEntry.setIndexNames(
    (0, "Novell-LANalyzer-Ext-MIB", "rpMacToIpHostIndex"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpMacToIpMACAddress"),
    (0, "Novell-LANalyzer-Ext-MIB", "rpMacToIpIPAddress"),
)
if mibBuilder.loadTexts:
    rpMacToIpEntry.setStatus("mandatory")


class _RpMacToIpHostIndex_Type(Integer32):
    """Custom type rpMacToIpHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpMacToIpHostIndex_Type.__name__ = "Integer32"
_RpMacToIpHostIndex_Object = MibTableColumn
rpMacToIpHostIndex = _RpMacToIpHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 4, 1, 1, 1),
    _RpMacToIpHostIndex_Type()
)
rpMacToIpHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMacToIpHostIndex.setStatus("mandatory")
_RpMacToIpMACAddress_Type = OctetString
_RpMacToIpMACAddress_Object = MibTableColumn
rpMacToIpMACAddress = _RpMacToIpMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 4, 1, 1, 2),
    _RpMacToIpMACAddress_Type()
)
rpMacToIpMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMacToIpMACAddress.setStatus("mandatory")
_RpMacToIpIPAddress_Type = IpAddress
_RpMacToIpIPAddress_Object = MibTableColumn
rpMacToIpIPAddress = _RpMacToIpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 13, 2, 4, 1, 1, 3),
    _RpMacToIpIPAddress_Type()
)
rpMacToIpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMacToIpIPAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

risingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 1)
)
risingAlarm.setObjects(
      *(("RFC1271-MIB", "alarmIndex"),
        ("RFC1271-MIB", "alarmVariable"),
        ("RFC1271-MIB", "alarmSampleType"),
        ("RFC1271-MIB", "alarmValue"),
        ("RFC1271-MIB", "alarmRisingThreshold"),
        ("Novell-LANalyzer-Ext-MIB", "rpAlarmRisingDescription"))
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus(
        ""
    )

fallingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 2)
)
fallingAlarm.setObjects(
      *(("RFC1271-MIB", "alarmIndex"),
        ("RFC1271-MIB", "alarmVariable"),
        ("RFC1271-MIB", "alarmSampleType"),
        ("RFC1271-MIB", "alarmValue"),
        ("RFC1271-MIB", "alarmFallingThreshold"),
        ("Novell-LANalyzer-Ext-MIB", "rpAlarmFallingDescription"))
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus(
        ""
    )

packetMatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 3)
)
packetMatch.setObjects(
      *(("RFC1271-MIB", "channelIndex"),
        ("RFC1271-MIB", "channelMatches"),
        ("RFC1271-MIB", "channelDescription"))
)
if mibBuilder.loadTexts:
    packetMatch.setStatus(
        ""
    )

rpHostActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 1, 1, 3, 0, 1)
)
rpHostActive.setObjects(
    ("Novell-LANalyzer-Ext-MIB", "rpHostMonitorAddress")
)
if mibBuilder.loadTexts:
    rpHostActive.setStatus(
        ""
    )

rpHostInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 1, 1, 3, 0, 2)
)
rpHostInactive.setObjects(
    ("Novell-LANalyzer-Ext-MIB", "rpHostMonitorAddress")
)
if mibBuilder.loadTexts:
    rpHostInactive.setStatus(
        ""
    )

rpDuplicateIpAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 1, 1, 3, 0, 3)
)
rpDuplicateIpAddr.setObjects(
      *(("Novell-LANalyzer-Ext-MIB", "rpDuplicateIpAddress"),
        ("Novell-LANalyzer-Ext-MIB", "rpDuplicateIpNewMAC"),
        ("Novell-LANalyzer-Ext-MIB", "rpDuplicateIpOldMAC"))
)
if mibBuilder.loadTexts:
    rpDuplicateIpAddr.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Novell-LANalyzer-Ext-MIB",
    **{"risingAlarm": risingAlarm,
       "fallingAlarm": fallingAlarm,
       "packetMatch": packetMatch,
       "novell": novell,
       "productType": productType,
       "lantern": lantern,
       "lantern-rmonPlus": lantern_rmonPlus,
       "rpHostActive": rpHostActive,
       "rpHostInactive": rpHostInactive,
       "rpDuplicateIpAddr": rpDuplicateIpAddr,
       "mibDoc": mibDoc,
       "rmonPlus-mib": rmonPlus_mib,
       "rmonShadow": rmonShadow,
       "rpAlarm": rpAlarm,
       "rpAlarmTable": rpAlarmTable,
       "rpAlarmEntry": rpAlarmEntry,
       "rpAlarmIndex": rpAlarmIndex,
       "rpAlarmRisingDescription": rpAlarmRisingDescription,
       "rpAlarmFallingDescription": rpAlarmFallingDescription,
       "rpHosts": rpHosts,
       "rpHostTable": rpHostTable,
       "rpHostEntry": rpHostEntry,
       "rpHostAddress": rpHostAddress,
       "rpHostCreationOrder": rpHostCreationOrder,
       "rpHostIndex": rpHostIndex,
       "rpHostProtocols": rpHostProtocols,
       "rpHostFirstTransmit": rpHostFirstTransmit,
       "rpHostLastTransmit": rpHostLastTransmit,
       "rpHostTimeTable": rpHostTimeTable,
       "rpHostTimeEntry": rpHostTimeEntry,
       "rpHostTimeAddress": rpHostTimeAddress,
       "rpHostTimeCreationOrder": rpHostTimeCreationOrder,
       "rpHostTimeIndex": rpHostTimeIndex,
       "rpHostTimeProtocols": rpHostTimeProtocols,
       "rpHostTimeFirstTransmit": rpHostTimeFirstTransmit,
       "rpHostTimeLastTransmit": rpHostTimeLastTransmit,
       "rpMatrix": rpMatrix,
       "rpMatrixSDTable": rpMatrixSDTable,
       "rpMatrixSDEntry": rpMatrixSDEntry,
       "rpMatrixSDSourceAddress": rpMatrixSDSourceAddress,
       "rpMatrixSDDestAddress": rpMatrixSDDestAddress,
       "rpMatrixSDIndex": rpMatrixSDIndex,
       "rpMatrixSDProtocols": rpMatrixSDProtocols,
       "rpMatrixSDFirstTransmit": rpMatrixSDFirstTransmit,
       "rpMatrixSDLastTransmit": rpMatrixSDLastTransmit,
       "rpMatrixDSTable": rpMatrixDSTable,
       "rpMatrixDSEntry": rpMatrixDSEntry,
       "rpMatrixDSSourceAddress": rpMatrixDSSourceAddress,
       "rpMatrixDSDestAddress": rpMatrixDSDestAddress,
       "rpMatrixDSIndex": rpMatrixDSIndex,
       "rpMatrixDSProtocols": rpMatrixDSProtocols,
       "rpMatrixDSFirstTransmit": rpMatrixDSFirstTransmit,
       "rpMatrixDSLastTransmit": rpMatrixDSLastTransmit,
       "rpFilter": rpFilter,
       "rpFilterTable": rpFilterTable,
       "rpFilterEntry": rpFilterEntry,
       "rpFilterIndex": rpFilterIndex,
       "rpFilterProtocols": rpFilterProtocols,
       "rpChannelTable": rpChannelTable,
       "rpChannelEntry": rpChannelEntry,
       "rpChannelIndex": rpChannelIndex,
       "rpChannelMatchOctets": rpChannelMatchOctets,
       "rpChannelControlBufferFull": rpChannelControlBufferFull,
       "rpBuffer": rpBuffer,
       "rpBufferControlTable": rpBufferControlTable,
       "rpBufferControlEntry": rpBufferControlEntry,
       "rpBufferControlIndex": rpBufferControlIndex,
       "rpBufferCaptureOctets": rpBufferCaptureOctets,
       "rmonExtensions": rmonExtensions,
       "rpAdmin": rpAdmin,
       "rpAdminSerialNumber": rpAdminSerialNumber,
       "rpAdminProbeCopies": rpAdminProbeCopies,
       "rpHostMonitor": rpHostMonitor,
       "rpHostMonitorControlTable": rpHostMonitorControlTable,
       "rpHostMonitorControlEntry": rpHostMonitorControlEntry,
       "rpHostMonitorControlIndex": rpHostMonitorControlIndex,
       "rpHostMonitorControlHostIndex": rpHostMonitorControlHostIndex,
       "rpHostMonitorControlActiveEvent": rpHostMonitorControlActiveEvent,
       "rpHostMonitorControlInactiveEvent": rpHostMonitorControlInactiveEvent,
       "rpHostMonitorControlTimeout": rpHostMonitorControlTimeout,
       "rpHostMonitorControlOwner": rpHostMonitorControlOwner,
       "rpHostMonitorControlStatus": rpHostMonitorControlStatus,
       "rpHostMonitorTable": rpHostMonitorTable,
       "rpHostMonitorEntry": rpHostMonitorEntry,
       "rpHostMonitorIndex": rpHostMonitorIndex,
       "rpHostMonitorAddress": rpHostMonitorAddress,
       "rpHostMonitorActivity": rpHostMonitorActivity,
       "rpHostMonitorAddDelete": rpHostMonitorAddDelete,
       "rpDuplicateIp": rpDuplicateIp,
       "rpDuplicateIpTable": rpDuplicateIpTable,
       "rpDuplicateIpEntry": rpDuplicateIpEntry,
       "rpDuplicateIpAddress": rpDuplicateIpAddress,
       "rpDuplicateIpNewMAC": rpDuplicateIpNewMAC,
       "rpDuplicateIpOldMAC": rpDuplicateIpOldMAC,
       "rpDuplicateIpTimestamp": rpDuplicateIpTimestamp,
       "rpMacToIp": rpMacToIp,
       "rpMacToIpTable": rpMacToIpTable,
       "rpMacToIpEntry": rpMacToIpEntry,
       "rpMacToIpHostIndex": rpMacToIpHostIndex,
       "rpMacToIpMACAddress": rpMacToIpMACAddress,
       "rpMacToIpIPAddress": rpMacToIpIPAddress}
)
