# SNMP MIB module (CABLE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABLE-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:12 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swCableDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 58)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwCableDiagCtrl_ObjectIdentity = ObjectIdentity
swCableDiagCtrl = _SwCableDiagCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1)
)
_SwEtherCableDiagTable_Object = MibTable
swEtherCableDiagTable = _SwEtherCableDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1)
)
if mibBuilder.loadTexts:
    swEtherCableDiagTable.setStatus("current")
_SwEtherCableDiagEntry_Object = MibTableRow
swEtherCableDiagEntry = _SwEtherCableDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1)
)
swEtherCableDiagEntry.setIndexNames(
    (0, "CABLE-DIAG-MIB", "swEtherCableDiagPortIndex"),
)
if mibBuilder.loadTexts:
    swEtherCableDiagEntry.setStatus("current")


class _SwEtherCableDiagPortIndex_Type(Integer32):
    """Custom type swEtherCableDiagPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwEtherCableDiagPortIndex_Type.__name__ = "Integer32"
_SwEtherCableDiagPortIndex_Object = MibTableColumn
swEtherCableDiagPortIndex = _SwEtherCableDiagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 1),
    _SwEtherCableDiagPortIndex_Type()
)
swEtherCableDiagPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPortIndex.setStatus("current")


class _SwEtherCableDiagPortType_Type(Integer32):
    """Custom type swEtherCableDiagPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 0),
          ("gigaEthernet", 1),
          ("other", 2))
    )


_SwEtherCableDiagPortType_Type.__name__ = "Integer32"
_SwEtherCableDiagPortType_Object = MibTableColumn
swEtherCableDiagPortType = _SwEtherCableDiagPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 2),
    _SwEtherCableDiagPortType_Type()
)
swEtherCableDiagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPortType.setStatus("current")


class _SwEtherCableDiagLinkStatus_Type(Integer32):
    """Custom type swEtherCableDiagLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1),
          ("other", 2))
    )


_SwEtherCableDiagLinkStatus_Type.__name__ = "Integer32"
_SwEtherCableDiagLinkStatus_Object = MibTableColumn
swEtherCableDiagLinkStatus = _SwEtherCableDiagLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 3),
    _SwEtherCableDiagLinkStatus_Type()
)
swEtherCableDiagLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagLinkStatus.setStatus("current")


class _SwEtherCableDiagPair1Status_Type(Integer32):
    """Custom type swEtherCableDiagPair1Status based on Integer32"""
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
        *(("count", 6),
          ("crosstalk", 4),
          ("no-cable", 7),
          ("ok", 0),
          ("open", 1),
          ("open-short", 3),
          ("other", 8),
          ("short", 2),
          ("unknown", 5))
    )


_SwEtherCableDiagPair1Status_Type.__name__ = "Integer32"
_SwEtherCableDiagPair1Status_Object = MibTableColumn
swEtherCableDiagPair1Status = _SwEtherCableDiagPair1Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 4),
    _SwEtherCableDiagPair1Status_Type()
)
swEtherCableDiagPair1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair1Status.setStatus("current")


class _SwEtherCableDiagPair2Status_Type(Integer32):
    """Custom type swEtherCableDiagPair2Status based on Integer32"""
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
        *(("count", 6),
          ("crosstalk", 4),
          ("no-cable", 7),
          ("ok", 0),
          ("open", 1),
          ("open-short", 3),
          ("other", 8),
          ("short", 2),
          ("unknown", 5))
    )


_SwEtherCableDiagPair2Status_Type.__name__ = "Integer32"
_SwEtherCableDiagPair2Status_Object = MibTableColumn
swEtherCableDiagPair2Status = _SwEtherCableDiagPair2Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 5),
    _SwEtherCableDiagPair2Status_Type()
)
swEtherCableDiagPair2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair2Status.setStatus("current")


class _SwEtherCableDiagPair3Status_Type(Integer32):
    """Custom type swEtherCableDiagPair3Status based on Integer32"""
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
        *(("count", 6),
          ("crosstalk", 4),
          ("no-cable", 7),
          ("ok", 0),
          ("open", 1),
          ("open-short", 3),
          ("other", 8),
          ("short", 2),
          ("unknown", 5))
    )


_SwEtherCableDiagPair3Status_Type.__name__ = "Integer32"
_SwEtherCableDiagPair3Status_Object = MibTableColumn
swEtherCableDiagPair3Status = _SwEtherCableDiagPair3Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 6),
    _SwEtherCableDiagPair3Status_Type()
)
swEtherCableDiagPair3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair3Status.setStatus("current")


class _SwEtherCableDiagPair4Status_Type(Integer32):
    """Custom type swEtherCableDiagPair4Status based on Integer32"""
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
        *(("count", 6),
          ("crosstalk", 4),
          ("no-cable", 7),
          ("ok", 0),
          ("open", 1),
          ("open-short", 3),
          ("other", 8),
          ("short", 2),
          ("unknown", 5))
    )


_SwEtherCableDiagPair4Status_Type.__name__ = "Integer32"
_SwEtherCableDiagPair4Status_Object = MibTableColumn
swEtherCableDiagPair4Status = _SwEtherCableDiagPair4Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 7),
    _SwEtherCableDiagPair4Status_Type()
)
swEtherCableDiagPair4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair4Status.setStatus("current")
_SwEtherCableDiagPair1Length_Type = Integer32
_SwEtherCableDiagPair1Length_Object = MibTableColumn
swEtherCableDiagPair1Length = _SwEtherCableDiagPair1Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 8),
    _SwEtherCableDiagPair1Length_Type()
)
swEtherCableDiagPair1Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair1Length.setStatus("current")
_SwEtherCableDiagPair2Length_Type = Integer32
_SwEtherCableDiagPair2Length_Object = MibTableColumn
swEtherCableDiagPair2Length = _SwEtherCableDiagPair2Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 9),
    _SwEtherCableDiagPair2Length_Type()
)
swEtherCableDiagPair2Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair2Length.setStatus("current")
_SwEtherCableDiagPair3Length_Type = Integer32
_SwEtherCableDiagPair3Length_Object = MibTableColumn
swEtherCableDiagPair3Length = _SwEtherCableDiagPair3Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 10),
    _SwEtherCableDiagPair3Length_Type()
)
swEtherCableDiagPair3Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair3Length.setStatus("current")
_SwEtherCableDiagPair4Length_Type = Integer32
_SwEtherCableDiagPair4Length_Object = MibTableColumn
swEtherCableDiagPair4Length = _SwEtherCableDiagPair4Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 11),
    _SwEtherCableDiagPair4Length_Type()
)
swEtherCableDiagPair4Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagPair4Length.setStatus("current")


class _SwEtherCableDiagAction_Type(Integer32):
    """Custom type swEtherCableDiagAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("action", 1),
          ("other", 3),
          ("processing", 2))
    )


_SwEtherCableDiagAction_Type.__name__ = "Integer32"
_SwEtherCableDiagAction_Object = MibTableColumn
swEtherCableDiagAction = _SwEtherCableDiagAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 12),
    _SwEtherCableDiagAction_Type()
)
swEtherCableDiagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEtherCableDiagAction.setStatus("current")


class _SwEtherCableDiagStatus_Type(Integer32):
    """Custom type swEtherCableDiagStatus based on Integer32"""
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
        *(("last-test-failed", 4),
          ("last-test-ok", 3),
          ("not-run", 1),
          ("processing", 2))
    )


_SwEtherCableDiagStatus_Type.__name__ = "Integer32"
_SwEtherCableDiagStatus_Object = MibTableColumn
swEtherCableDiagStatus = _SwEtherCableDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 58, 1, 1, 1, 13),
    _SwEtherCableDiagStatus_Type()
)
swEtherCableDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherCableDiagStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABLE-DIAG-MIB",
    **{"swCableDiagMIB": swCableDiagMIB,
       "swCableDiagCtrl": swCableDiagCtrl,
       "swEtherCableDiagTable": swEtherCableDiagTable,
       "swEtherCableDiagEntry": swEtherCableDiagEntry,
       "swEtherCableDiagPortIndex": swEtherCableDiagPortIndex,
       "swEtherCableDiagPortType": swEtherCableDiagPortType,
       "swEtherCableDiagLinkStatus": swEtherCableDiagLinkStatus,
       "swEtherCableDiagPair1Status": swEtherCableDiagPair1Status,
       "swEtherCableDiagPair2Status": swEtherCableDiagPair2Status,
       "swEtherCableDiagPair3Status": swEtherCableDiagPair3Status,
       "swEtherCableDiagPair4Status": swEtherCableDiagPair4Status,
       "swEtherCableDiagPair1Length": swEtherCableDiagPair1Length,
       "swEtherCableDiagPair2Length": swEtherCableDiagPair2Length,
       "swEtherCableDiagPair3Length": swEtherCableDiagPair3Length,
       "swEtherCableDiagPair4Length": swEtherCableDiagPair4Length,
       "swEtherCableDiagAction": swEtherCableDiagAction,
       "swEtherCableDiagStatus": swEtherCableDiagStatus}
)
