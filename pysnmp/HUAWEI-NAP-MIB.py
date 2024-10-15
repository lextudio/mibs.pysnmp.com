# SNMP MIB module (HUAWEI-NAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-NAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:19 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention,
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
    "TextualConvention",
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

hwNap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206)
)
hwNap.setRevisions(
        ("2009-03-17 10:27",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



# MIB Managed Objects in the order of their OIDs

_HwNapScalarObjects_ObjectIdentity = ObjectIdentity
hwNapScalarObjects = _HwNapScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 1)
)
_HwNapNeighborNum_Type = Integer32
_HwNapNeighborNum_Object = MibScalar
hwNapNeighborNum = _HwNapNeighborNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 1, 1),
    _HwNapNeighborNum_Type()
)
hwNapNeighborNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNapNeighborNum.setStatus("current")
_HwNapTableObjects_ObjectIdentity = ObjectIdentity
hwNapTableObjects = _HwNapTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2)
)
_HwNapNeighborTable_Object = MibTable
hwNapNeighborTable = _HwNapNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1)
)
if mibBuilder.loadTexts:
    hwNapNeighborTable.setStatus("current")
_HwNapNeighborEntry_Object = MibTableRow
hwNapNeighborEntry = _HwNapNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1)
)
hwNapNeighborEntry.setIndexNames(
    (0, "HUAWEI-NAP-MIB", "hwNapNeighborIndex"),
)
if mibBuilder.loadTexts:
    hwNapNeighborEntry.setStatus("current")


class _HwNapNeighborIndex_Type(Integer32):
    """Custom type hwNapNeighborIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwNapNeighborIndex_Type.__name__ = "Integer32"
_HwNapNeighborIndex_Object = MibTableColumn
hwNapNeighborIndex = _HwNapNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 1),
    _HwNapNeighborIndex_Type()
)
hwNapNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNapNeighborIndex.setStatus("current")
_HwNapLocalPortName_Type = OctetString
_HwNapLocalPortName_Object = MibTableColumn
hwNapLocalPortName = _HwNapLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 2),
    _HwNapLocalPortName_Type()
)
hwNapLocalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNapLocalPortName.setStatus("current")


class _HwNapNeighborStatus_Type(Integer32):
    """Custom type hwNapNeighborStatus based on Integer32"""
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
        *(("abnormal", 4),
          ("detecting", 1),
          ("established", 2),
          ("ipAssigned", 3))
    )


_HwNapNeighborStatus_Type.__name__ = "Integer32"
_HwNapNeighborStatus_Object = MibTableColumn
hwNapNeighborStatus = _HwNapNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 3),
    _HwNapNeighborStatus_Type()
)
hwNapNeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNapNeighborStatus.setStatus("current")


class _HwNapNeighborAbnormalReason_Type(Integer32):
    """Custom type hwNapNeighborAbnormalReason based on Integer32"""
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
        *(("masterIpAssignError", 3),
          ("normal", 0),
          ("portNotSupport", 1),
          ("slaveDisable", 2),
          ("slaveIpAssignError", 4))
    )


_HwNapNeighborAbnormalReason_Type.__name__ = "Integer32"
_HwNapNeighborAbnormalReason_Object = MibTableColumn
hwNapNeighborAbnormalReason = _HwNapNeighborAbnormalReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 4),
    _HwNapNeighborAbnormalReason_Type()
)
hwNapNeighborAbnormalReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNapNeighborAbnormalReason.setStatus("current")
_HwNapNotifications_ObjectIdentity = ObjectIdentity
hwNapNotifications = _HwNapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 3)
)

# Managed Objects groups


# Notification objects

hwNapStatusNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 3, 1)
)
hwNapStatusNotify.setObjects(
      *(("HUAWEI-NAP-MIB", "hwNapLocalPortName"),
        ("HUAWEI-NAP-MIB", "hwNapNeighborStatus"),
        ("HUAWEI-NAP-MIB", "hwNapNeighborAbnormalReason"))
)
if mibBuilder.loadTexts:
    hwNapStatusNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-NAP-MIB",
    **{"DateAndTime": DateAndTime,
       "hwNap": hwNap,
       "hwNapScalarObjects": hwNapScalarObjects,
       "hwNapNeighborNum": hwNapNeighborNum,
       "hwNapTableObjects": hwNapTableObjects,
       "hwNapNeighborTable": hwNapNeighborTable,
       "hwNapNeighborEntry": hwNapNeighborEntry,
       "hwNapNeighborIndex": hwNapNeighborIndex,
       "hwNapLocalPortName": hwNapLocalPortName,
       "hwNapNeighborStatus": hwNapNeighborStatus,
       "hwNapNeighborAbnormalReason": hwNapNeighborAbnormalReason,
       "hwNapNotifications": hwNapNotifications,
       "hwNapStatusNotify": hwNapStatusNotify}
)
