# SNMP MIB module (H3C-MIRRORGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-MIRRORGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:57 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cMirrGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68)
)
h3cMirrGroup.setRevisions(
        ("2006-01-10 19:03",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMGInfoObjects_ObjectIdentity = ObjectIdentity
h3cMGInfoObjects = _H3cMGInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1)
)
_H3cMGObjects_ObjectIdentity = ObjectIdentity
h3cMGObjects = _H3cMGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1)
)
_H3cMGTable_Object = MibTable
h3cMGTable = _H3cMGTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cMGTable.setStatus("current")
_H3cMGEntry_Object = MibTableRow
h3cMGEntry = _H3cMGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1)
)
h3cMGEntry.setIndexNames(
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGID"),
)
if mibBuilder.loadTexts:
    h3cMGEntry.setStatus("current")
_H3cMGID_Type = Integer32
_H3cMGID_Object = MibTableColumn
h3cMGID = _H3cMGID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 1),
    _H3cMGID_Type()
)
h3cMGID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMGID.setStatus("current")


class _H3cMGType_Type(Integer32):
    """Custom type h3cMGType based on Integer32"""
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


_H3cMGType_Type.__name__ = "Integer32"
_H3cMGType_Object = MibTableColumn
h3cMGType = _H3cMGType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 2),
    _H3cMGType_Type()
)
h3cMGType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMGType.setStatus("current")


class _H3cMGStatus_Type(Integer32):
    """Custom type h3cMGStatus based on Integer32"""
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


_H3cMGStatus_Type.__name__ = "Integer32"
_H3cMGStatus_Object = MibTableColumn
h3cMGStatus = _H3cMGStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 3),
    _H3cMGStatus_Type()
)
h3cMGStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMGStatus.setStatus("current")
_H3cMGRowStatus_Type = RowStatus
_H3cMGRowStatus_Object = MibTableColumn
h3cMGRowStatus = _H3cMGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 4),
    _H3cMGRowStatus_Type()
)
h3cMGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMGRowStatus.setStatus("current")
_H3cMGMirrorIfObjects_ObjectIdentity = ObjectIdentity
h3cMGMirrorIfObjects = _H3cMGMirrorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2)
)
_H3cMGMirrorIfTable_Object = MibTable
h3cMGMirrorIfTable = _H3cMGMirrorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMGMirrorIfTable.setStatus("current")
_H3cMGMirrorIfEntry_Object = MibTableRow
h3cMGMirrorIfEntry = _H3cMGMirrorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1)
)
h3cMGMirrorIfEntry.setIndexNames(
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGID"),
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGMirrorIfIndex"),
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGMirrorDirection"),
)
if mibBuilder.loadTexts:
    h3cMGMirrorIfEntry.setStatus("current")
_H3cMGMirrorIfIndex_Type = Integer32
_H3cMGMirrorIfIndex_Object = MibTableColumn
h3cMGMirrorIfIndex = _H3cMGMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1, 1),
    _H3cMGMirrorIfIndex_Type()
)
h3cMGMirrorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMGMirrorIfIndex.setStatus("current")


class _H3cMGMirrorDirection_Type(Integer32):
    """Custom type h3cMGMirrorDirection based on Integer32"""
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


_H3cMGMirrorDirection_Type.__name__ = "Integer32"
_H3cMGMirrorDirection_Object = MibTableColumn
h3cMGMirrorDirection = _H3cMGMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1, 2),
    _H3cMGMirrorDirection_Type()
)
h3cMGMirrorDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMGMirrorDirection.setStatus("current")
_H3cMGMirrorRowStatus_Type = RowStatus
_H3cMGMirrorRowStatus_Object = MibTableColumn
h3cMGMirrorRowStatus = _H3cMGMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1, 3),
    _H3cMGMirrorRowStatus_Type()
)
h3cMGMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMGMirrorRowStatus.setStatus("current")
_H3cMGMonitorIfObjects_ObjectIdentity = ObjectIdentity
h3cMGMonitorIfObjects = _H3cMGMonitorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3)
)
_H3cMGMonitorIfTable_Object = MibTable
h3cMGMonitorIfTable = _H3cMGMonitorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cMGMonitorIfTable.setStatus("current")
_H3cMGMonitorIfEntry_Object = MibTableRow
h3cMGMonitorIfEntry = _H3cMGMonitorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1, 1)
)
h3cMGMonitorIfEntry.setIndexNames(
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGID"),
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    h3cMGMonitorIfEntry.setStatus("current")
_H3cMGMonitorIfIndex_Type = Integer32
_H3cMGMonitorIfIndex_Object = MibTableColumn
h3cMGMonitorIfIndex = _H3cMGMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1, 1, 1),
    _H3cMGMonitorIfIndex_Type()
)
h3cMGMonitorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMGMonitorIfIndex.setStatus("current")
_H3cMGMonitorRowStatus_Type = RowStatus
_H3cMGMonitorRowStatus_Object = MibTableColumn
h3cMGMonitorRowStatus = _H3cMGMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1, 1, 2),
    _H3cMGMonitorRowStatus_Type()
)
h3cMGMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMGMonitorRowStatus.setStatus("current")
_H3cMGReflectorIfObjects_ObjectIdentity = ObjectIdentity
h3cMGReflectorIfObjects = _H3cMGReflectorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4)
)
_H3cMGReflectorIfTable_Object = MibTable
h3cMGReflectorIfTable = _H3cMGReflectorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cMGReflectorIfTable.setStatus("current")
_H3cMGReflectorIfEntry_Object = MibTableRow
h3cMGReflectorIfEntry = _H3cMGReflectorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1, 1)
)
h3cMGReflectorIfEntry.setIndexNames(
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGID"),
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGReflectorIfIndex"),
)
if mibBuilder.loadTexts:
    h3cMGReflectorIfEntry.setStatus("current")
_H3cMGReflectorIfIndex_Type = Integer32
_H3cMGReflectorIfIndex_Object = MibTableColumn
h3cMGReflectorIfIndex = _H3cMGReflectorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1, 1, 1),
    _H3cMGReflectorIfIndex_Type()
)
h3cMGReflectorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMGReflectorIfIndex.setStatus("current")
_H3cMGReflectorRowStatus_Type = RowStatus
_H3cMGReflectorRowStatus_Object = MibTableColumn
h3cMGReflectorRowStatus = _H3cMGReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1, 1, 2),
    _H3cMGReflectorRowStatus_Type()
)
h3cMGReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMGReflectorRowStatus.setStatus("current")
_H3cMGRprobeVlanObjects_ObjectIdentity = ObjectIdentity
h3cMGRprobeVlanObjects = _H3cMGRprobeVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5)
)
_H3cMGRprobeVlanTable_Object = MibTable
h3cMGRprobeVlanTable = _H3cMGRprobeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cMGRprobeVlanTable.setStatus("current")
_H3cMGRprobeVlanEntry_Object = MibTableRow
h3cMGRprobeVlanEntry = _H3cMGRprobeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1, 1)
)
h3cMGRprobeVlanEntry.setIndexNames(
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGID"),
    (0, "H3C-MIRRORGROUP-MIB", "h3cMGRprobeVlanID"),
)
if mibBuilder.loadTexts:
    h3cMGRprobeVlanEntry.setStatus("current")


class _H3cMGRprobeVlanID_Type(Integer32):
    """Custom type h3cMGRprobeVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cMGRprobeVlanID_Type.__name__ = "Integer32"
_H3cMGRprobeVlanID_Object = MibTableColumn
h3cMGRprobeVlanID = _H3cMGRprobeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1, 1, 1),
    _H3cMGRprobeVlanID_Type()
)
h3cMGRprobeVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMGRprobeVlanID.setStatus("current")
_H3cMGRprobeVlanRowStatus_Type = RowStatus
_H3cMGRprobeVlanRowStatus_Object = MibTableColumn
h3cMGRprobeVlanRowStatus = _H3cMGRprobeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1, 1, 2),
    _H3cMGRprobeVlanRowStatus_Type()
)
h3cMGRprobeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMGRprobeVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MIRRORGROUP-MIB",
    **{"h3cMirrGroup": h3cMirrGroup,
       "h3cMGInfoObjects": h3cMGInfoObjects,
       "h3cMGObjects": h3cMGObjects,
       "h3cMGTable": h3cMGTable,
       "h3cMGEntry": h3cMGEntry,
       "h3cMGID": h3cMGID,
       "h3cMGType": h3cMGType,
       "h3cMGStatus": h3cMGStatus,
       "h3cMGRowStatus": h3cMGRowStatus,
       "h3cMGMirrorIfObjects": h3cMGMirrorIfObjects,
       "h3cMGMirrorIfTable": h3cMGMirrorIfTable,
       "h3cMGMirrorIfEntry": h3cMGMirrorIfEntry,
       "h3cMGMirrorIfIndex": h3cMGMirrorIfIndex,
       "h3cMGMirrorDirection": h3cMGMirrorDirection,
       "h3cMGMirrorRowStatus": h3cMGMirrorRowStatus,
       "h3cMGMonitorIfObjects": h3cMGMonitorIfObjects,
       "h3cMGMonitorIfTable": h3cMGMonitorIfTable,
       "h3cMGMonitorIfEntry": h3cMGMonitorIfEntry,
       "h3cMGMonitorIfIndex": h3cMGMonitorIfIndex,
       "h3cMGMonitorRowStatus": h3cMGMonitorRowStatus,
       "h3cMGReflectorIfObjects": h3cMGReflectorIfObjects,
       "h3cMGReflectorIfTable": h3cMGReflectorIfTable,
       "h3cMGReflectorIfEntry": h3cMGReflectorIfEntry,
       "h3cMGReflectorIfIndex": h3cMGReflectorIfIndex,
       "h3cMGReflectorRowStatus": h3cMGReflectorRowStatus,
       "h3cMGRprobeVlanObjects": h3cMGRprobeVlanObjects,
       "h3cMGRprobeVlanTable": h3cMGRprobeVlanTable,
       "h3cMGRprobeVlanEntry": h3cMGRprobeVlanEntry,
       "h3cMGRprobeVlanID": h3cMGRprobeVlanID,
       "h3cMGRprobeVlanRowStatus": h3cMGRprobeVlanRowStatus}
)
