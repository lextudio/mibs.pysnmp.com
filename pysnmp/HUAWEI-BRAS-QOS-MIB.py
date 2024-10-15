# SNMP MIB module (HUAWEI-BRAS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:05 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

hwBRASQoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SchedulerStyle(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2))
    )



class QueueClass(Integer32, TextualConvention):
    status = "current"
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )



class SchedulerService(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )



class InterfaceScheduler(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("location", 1),
          ("none", 2),
          ("servicegroup", 3))
    )



class LinkMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cell", 3),
          ("frame", 2),
          ("none", 1))
    )



class StatMode(Integer32, TextualConvention):
    status = "current"
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
        *(("after", 3),
          ("before", 2),
          ("both", 4),
          ("none", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwBRASQoSObjects_ObjectIdentity = ObjectIdentity
hwBRASQoSObjects = _HwBRASQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1)
)
_HwBRASQoSQoSProfileTable_Object = MibTable
hwBRASQoSQoSProfileTable = _HwBRASQoSQoSProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1)
)
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileTable.setStatus("current")
_HwBRASQoSQoSProfileEntry_Object = MibTableRow
hwBRASQoSQoSProfileEntry = _HwBRASQoSQoSProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1)
)
hwBRASQoSQoSProfileEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileEntry.setStatus("current")


class _HwBRASQoSQoSProfileIndex_Type(Integer32):
    """Custom type hwBRASQoSQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBRASQoSQoSProfileIndex_Type.__name__ = "Integer32"
_HwBRASQoSQoSProfileIndex_Object = MibTableColumn
hwBRASQoSQoSProfileIndex = _HwBRASQoSQoSProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 1),
    _HwBRASQoSQoSProfileIndex_Type()
)
hwBRASQoSQoSProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileIndex.setStatus("current")


class _HwBRASQoSQoSProfileName_Type(OctetString):
    """Custom type hwBRASQoSQoSProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQoSProfileName_Type.__name__ = "OctetString"
_HwBRASQoSQoSProfileName_Object = MibTableColumn
hwBRASQoSQoSProfileName = _HwBRASQoSQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 2),
    _HwBRASQoSQoSProfileName_Type()
)
hwBRASQoSQoSProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileName.setStatus("current")


class _HwBRASQoSQoSProfileQueueName_Type(OctetString):
    """Custom type hwBRASQoSQoSProfileQueueName based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQoSProfileQueueName_Type.__name__ = "OctetString"
_HwBRASQoSQoSProfileQueueName_Object = MibTableColumn
hwBRASQoSQoSProfileQueueName = _HwBRASQoSQoSProfileQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 3),
    _HwBRASQoSQoSProfileQueueName_Type()
)
hwBRASQoSQoSProfileQueueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileQueueName.setStatus("current")


class _HwBRASQoSQoSProfileDropName_Type(OctetString):
    """Custom type hwBRASQoSQoSProfileDropName based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQoSProfileDropName_Type.__name__ = "OctetString"
_HwBRASQoSQoSProfileDropName_Object = MibTableColumn
hwBRASQoSQoSProfileDropName = _HwBRASQoSQoSProfileDropName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 4),
    _HwBRASQoSQoSProfileDropName_Type()
)
hwBRASQoSQoSProfileDropName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileDropName.setStatus("current")


class _HwBRASQoSQoSProfileSchedulerName_Type(OctetString):
    """Custom type hwBRASQoSQoSProfileSchedulerName based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQoSProfileSchedulerName_Type.__name__ = "OctetString"
_HwBRASQoSQoSProfileSchedulerName_Object = MibTableColumn
hwBRASQoSQoSProfileSchedulerName = _HwBRASQoSQoSProfileSchedulerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 5),
    _HwBRASQoSQoSProfileSchedulerName_Type()
)
hwBRASQoSQoSProfileSchedulerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileSchedulerName.setStatus("current")


class _HwBRASQoSQoSFlowMappingName_Type(OctetString):
    """Custom type hwBRASQoSQoSFlowMappingName based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQoSFlowMappingName_Type.__name__ = "OctetString"
_HwBRASQoSQoSFlowMappingName_Object = MibTableColumn
hwBRASQoSQoSFlowMappingName = _HwBRASQoSQoSFlowMappingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 6),
    _HwBRASQoSQoSFlowMappingName_Type()
)
hwBRASQoSQoSFlowMappingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSFlowMappingName.setStatus("current")


class _HwBRASQoSQoSLinkAjustLength_Type(OctetString):
    """Custom type hwBRASQoSQoSLinkAjustLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQoSLinkAjustLength_Type.__name__ = "OctetString"
_HwBRASQoSQoSLinkAjustLength_Object = MibTableColumn
hwBRASQoSQoSLinkAjustLength = _HwBRASQoSQoSLinkAjustLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 7),
    _HwBRASQoSQoSLinkAjustLength_Type()
)
hwBRASQoSQoSLinkAjustLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSLinkAjustLength.setStatus("current")
_HwBRASQoSQoSProfileRowStatus_Type = RowStatus
_HwBRASQoSQoSProfileRowStatus_Object = MibTableColumn
hwBRASQoSQoSProfileRowStatus = _HwBRASQoSQoSProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 1, 1, 8),
    _HwBRASQoSQoSProfileRowStatus_Type()
)
hwBRASQoSQoSProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQoSProfileRowStatus.setStatus("current")
_HwBRASQoSSchedulerProfileTable_Object = MibTable
hwBRASQoSSchedulerProfileTable = _HwBRASQoSSchedulerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2)
)
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileTable.setStatus("current")
_HwBRASQoSSchedulerProfileEntry_Object = MibTableRow
hwBRASQoSSchedulerProfileEntry = _HwBRASQoSSchedulerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1)
)
hwBRASQoSSchedulerProfileEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileEntry.setStatus("current")


class _HwBRASQoSSchedulerProfileIndex_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBRASQoSSchedulerProfileIndex_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileIndex_Object = MibTableColumn
hwBRASQoSSchedulerProfileIndex = _HwBRASQoSSchedulerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 1),
    _HwBRASQoSSchedulerProfileIndex_Type()
)
hwBRASQoSSchedulerProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileIndex.setStatus("current")


class _HwBRASQoSSchedulerProfileName_Type(OctetString):
    """Custom type hwBRASQoSSchedulerProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSSchedulerProfileName_Type.__name__ = "OctetString"
_HwBRASQoSSchedulerProfileName_Object = MibTableColumn
hwBRASQoSSchedulerProfileName = _HwBRASQoSSchedulerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 2),
    _HwBRASQoSSchedulerProfileName_Type()
)
hwBRASQoSSchedulerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileName.setStatus("current")


class _HwBRASQoSSchedulerProfileGtsUpCir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileGtsUpCir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 10000000),
    )


_HwBRASQoSSchedulerProfileGtsUpCir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileGtsUpCir_Object = MibTableColumn
hwBRASQoSSchedulerProfileGtsUpCir = _HwBRASQoSSchedulerProfileGtsUpCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 3),
    _HwBRASQoSSchedulerProfileGtsUpCir_Type()
)
hwBRASQoSSchedulerProfileGtsUpCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileGtsUpCir.setStatus("current")


class _HwBRASQoSSchedulerProfileGtsUpPir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileGtsUpPir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10000000),
    )


_HwBRASQoSSchedulerProfileGtsUpPir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileGtsUpPir_Object = MibTableColumn
hwBRASQoSSchedulerProfileGtsUpPir = _HwBRASQoSSchedulerProfileGtsUpPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 4),
    _HwBRASQoSSchedulerProfileGtsUpPir_Type()
)
hwBRASQoSSchedulerProfileGtsUpPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileGtsUpPir.setStatus("current")


class _HwBRASQoSSchedulerProfileGtsUpLength_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileGtsUpLength based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 128000),
    )


_HwBRASQoSSchedulerProfileGtsUpLength_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileGtsUpLength_Object = MibTableColumn
hwBRASQoSSchedulerProfileGtsUpLength = _HwBRASQoSSchedulerProfileGtsUpLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 5),
    _HwBRASQoSSchedulerProfileGtsUpLength_Type()
)
hwBRASQoSSchedulerProfileGtsUpLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileGtsUpLength.setStatus("current")


class _HwBRASQoSSchedulerProfileGtsDownCir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileGtsDownCir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 1000000),
    )


_HwBRASQoSSchedulerProfileGtsDownCir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileGtsDownCir_Object = MibTableColumn
hwBRASQoSSchedulerProfileGtsDownCir = _HwBRASQoSSchedulerProfileGtsDownCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 6),
    _HwBRASQoSSchedulerProfileGtsDownCir_Type()
)
hwBRASQoSSchedulerProfileGtsDownCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileGtsDownCir.setStatus("current")


class _HwBRASQoSSchedulerProfileGtsDownPir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileGtsDownPir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_HwBRASQoSSchedulerProfileGtsDownPir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileGtsDownPir_Object = MibTableColumn
hwBRASQoSSchedulerProfileGtsDownPir = _HwBRASQoSSchedulerProfileGtsDownPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 7),
    _HwBRASQoSSchedulerProfileGtsDownPir_Type()
)
hwBRASQoSSchedulerProfileGtsDownPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileGtsDownPir.setStatus("current")


class _HwBRASQoSSchedulerProfileGtsDownLength_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileGtsDownLength based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 128000),
    )


_HwBRASQoSSchedulerProfileGtsDownLength_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileGtsDownLength_Object = MibTableColumn
hwBRASQoSSchedulerProfileGtsDownLength = _HwBRASQoSSchedulerProfileGtsDownLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 8),
    _HwBRASQoSSchedulerProfileGtsDownLength_Type()
)
hwBRASQoSSchedulerProfileGtsDownLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileGtsDownLength.setStatus("current")


class _HwBRASQoSSchedulerProfileUpCir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileUpCir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 1000000),
    )


_HwBRASQoSSchedulerProfileUpCir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileUpCir_Object = MibTableColumn
hwBRASQoSSchedulerProfileUpCir = _HwBRASQoSSchedulerProfileUpCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 9),
    _HwBRASQoSSchedulerProfileUpCir_Type()
)
hwBRASQoSSchedulerProfileUpCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileUpCir.setStatus("current")


class _HwBRASQoSSchedulerProfileUpCbs_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileUpCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10000, 8388608),
    )


_HwBRASQoSSchedulerProfileUpCbs_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileUpCbs_Object = MibTableColumn
hwBRASQoSSchedulerProfileUpCbs = _HwBRASQoSSchedulerProfileUpCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 10),
    _HwBRASQoSSchedulerProfileUpCbs_Type()
)
hwBRASQoSSchedulerProfileUpCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileUpCbs.setStatus("current")


class _HwBRASQoSSchedulerProfileUpPir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileUpPir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 1000000),
    )


_HwBRASQoSSchedulerProfileUpPir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileUpPir_Object = MibTableColumn
hwBRASQoSSchedulerProfileUpPir = _HwBRASQoSSchedulerProfileUpPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 11),
    _HwBRASQoSSchedulerProfileUpPir_Type()
)
hwBRASQoSSchedulerProfileUpPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileUpPir.setStatus("current")


class _HwBRASQoSSchedulerProfileUpPbs_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileUpPbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10000, 8388608),
    )


_HwBRASQoSSchedulerProfileUpPbs_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileUpPbs_Object = MibTableColumn
hwBRASQoSSchedulerProfileUpPbs = _HwBRASQoSSchedulerProfileUpPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 12),
    _HwBRASQoSSchedulerProfileUpPbs_Type()
)
hwBRASQoSSchedulerProfileUpPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileUpPbs.setStatus("current")


class _HwBRASQoSSchedulerProfileDownCir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileDownCir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 10000000),
    )


_HwBRASQoSSchedulerProfileDownCir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileDownCir_Object = MibTableColumn
hwBRASQoSSchedulerProfileDownCir = _HwBRASQoSSchedulerProfileDownCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 13),
    _HwBRASQoSSchedulerProfileDownCir_Type()
)
hwBRASQoSSchedulerProfileDownCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileDownCir.setStatus("current")


class _HwBRASQoSSchedulerProfileDownCbs_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileDownCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10000, 8388608),
    )


_HwBRASQoSSchedulerProfileDownCbs_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileDownCbs_Object = MibTableColumn
hwBRASQoSSchedulerProfileDownCbs = _HwBRASQoSSchedulerProfileDownCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 14),
    _HwBRASQoSSchedulerProfileDownCbs_Type()
)
hwBRASQoSSchedulerProfileDownCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileDownCbs.setStatus("current")


class _HwBRASQoSSchedulerProfileDownPir_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileDownPir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 1000000),
    )


_HwBRASQoSSchedulerProfileDownPir_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileDownPir_Object = MibTableColumn
hwBRASQoSSchedulerProfileDownPir = _HwBRASQoSSchedulerProfileDownPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 15),
    _HwBRASQoSSchedulerProfileDownPir_Type()
)
hwBRASQoSSchedulerProfileDownPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileDownPir.setStatus("current")


class _HwBRASQoSSchedulerProfileDownPbs_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileDownPbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10000, 8388608),
    )


_HwBRASQoSSchedulerProfileDownPbs_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileDownPbs_Object = MibTableColumn
hwBRASQoSSchedulerProfileDownPbs = _HwBRASQoSSchedulerProfileDownPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 16),
    _HwBRASQoSSchedulerProfileDownPbs_Type()
)
hwBRASQoSSchedulerProfileDownPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileDownPbs.setStatus("current")


class _HwBRASQoSSchedulerProfileWfqWeight_Type(Integer32):
    """Custom type hwBRASQoSSchedulerProfileWfqWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HwBRASQoSSchedulerProfileWfqWeight_Type.__name__ = "Integer32"
_HwBRASQoSSchedulerProfileWfqWeight_Object = MibTableColumn
hwBRASQoSSchedulerProfileWfqWeight = _HwBRASQoSSchedulerProfileWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 17),
    _HwBRASQoSSchedulerProfileWfqWeight_Type()
)
hwBRASQoSSchedulerProfileWfqWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerProfileWfqWeight.setStatus("current")
_HwBRASQoSSchedulerRowStatus_Type = RowStatus
_HwBRASQoSSchedulerRowStatus_Object = MibTableColumn
hwBRASQoSSchedulerRowStatus = _HwBRASQoSSchedulerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 2, 1, 18),
    _HwBRASQoSSchedulerRowStatus_Type()
)
hwBRASQoSSchedulerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSSchedulerRowStatus.setStatus("current")
_HwBRASQoSDropProfileTable_Object = MibTable
hwBRASQoSDropProfileTable = _HwBRASQoSDropProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3)
)
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTable.setStatus("current")
_HwBRASQoSDropProfileEntry_Object = MibTableRow
hwBRASQoSDropProfileEntry = _HwBRASQoSDropProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1)
)
hwBRASQoSDropProfileEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileEntry.setStatus("current")


class _HwBRASQoSDropProfileIndex_Type(Integer32):
    """Custom type hwBRASQoSDropProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwBRASQoSDropProfileIndex_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileIndex_Object = MibTableColumn
hwBRASQoSDropProfileIndex = _HwBRASQoSDropProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 1),
    _HwBRASQoSDropProfileIndex_Type()
)
hwBRASQoSDropProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileIndex.setStatus("current")


class _HwBRASQoSDropProfileName_Type(OctetString):
    """Custom type hwBRASQoSDropProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSDropProfileName_Type.__name__ = "OctetString"
_HwBRASQoSDropProfileName_Object = MibTableColumn
hwBRASQoSDropProfileName = _HwBRASQoSDropProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 2),
    _HwBRASQoSDropProfileName_Type()
)
hwBRASQoSDropProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileName.setStatus("current")


class _HwBRASQoSDropProfileTailBeThreshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailBeThreshold based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailBeThreshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailBeThreshold_Object = MibTableColumn
hwBRASQoSDropProfileTailBeThreshold = _HwBRASQoSDropProfileTailBeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 3),
    _HwBRASQoSDropProfileTailBeThreshold_Type()
)
hwBRASQoSDropProfileTailBeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailBeThreshold.setStatus("current")


class _HwBRASQoSDropProfileTailAf1Threshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailAf1Threshold based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailAf1Threshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailAf1Threshold_Object = MibTableColumn
hwBRASQoSDropProfileTailAf1Threshold = _HwBRASQoSDropProfileTailAf1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 4),
    _HwBRASQoSDropProfileTailAf1Threshold_Type()
)
hwBRASQoSDropProfileTailAf1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailAf1Threshold.setStatus("current")


class _HwBRASQoSDropProfileTailAf2Threshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailAf2Threshold based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailAf2Threshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailAf2Threshold_Object = MibTableColumn
hwBRASQoSDropProfileTailAf2Threshold = _HwBRASQoSDropProfileTailAf2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 5),
    _HwBRASQoSDropProfileTailAf2Threshold_Type()
)
hwBRASQoSDropProfileTailAf2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailAf2Threshold.setStatus("current")


class _HwBRASQoSDropProfileTailAf3Threshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailAf3Threshold based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailAf3Threshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailAf3Threshold_Object = MibTableColumn
hwBRASQoSDropProfileTailAf3Threshold = _HwBRASQoSDropProfileTailAf3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 6),
    _HwBRASQoSDropProfileTailAf3Threshold_Type()
)
hwBRASQoSDropProfileTailAf3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailAf3Threshold.setStatus("current")


class _HwBRASQoSDropProfileTailAf4Threshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailAf4Threshold based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailAf4Threshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailAf4Threshold_Object = MibTableColumn
hwBRASQoSDropProfileTailAf4Threshold = _HwBRASQoSDropProfileTailAf4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 7),
    _HwBRASQoSDropProfileTailAf4Threshold_Type()
)
hwBRASQoSDropProfileTailAf4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailAf4Threshold.setStatus("current")


class _HwBRASQoSDropProfileTailEfThreshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailEfThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailEfThreshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailEfThreshold_Object = MibTableColumn
hwBRASQoSDropProfileTailEfThreshold = _HwBRASQoSDropProfileTailEfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 8),
    _HwBRASQoSDropProfileTailEfThreshold_Type()
)
hwBRASQoSDropProfileTailEfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailEfThreshold.setStatus("current")


class _HwBRASQoSDropProfileTailCs6Threshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailCs6Threshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailCs6Threshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailCs6Threshold_Object = MibTableColumn
hwBRASQoSDropProfileTailCs6Threshold = _HwBRASQoSDropProfileTailCs6Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 9),
    _HwBRASQoSDropProfileTailCs6Threshold_Type()
)
hwBRASQoSDropProfileTailCs6Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailCs6Threshold.setStatus("current")


class _HwBRASQoSDropProfileTailCs7Threshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileTailCs7Threshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileTailCs7Threshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileTailCs7Threshold_Object = MibTableColumn
hwBRASQoSDropProfileTailCs7Threshold = _HwBRASQoSDropProfileTailCs7Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 10),
    _HwBRASQoSDropProfileTailCs7Threshold_Type()
)
hwBRASQoSDropProfileTailCs7Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileTailCs7Threshold.setStatus("current")


class _HwBRASQoSDropProfileWredMaxThreshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredMaxThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileWredMaxThreshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredMaxThreshold_Object = MibTableColumn
hwBRASQoSDropProfileWredMaxThreshold = _HwBRASQoSDropProfileWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 11),
    _HwBRASQoSDropProfileWredMaxThreshold_Type()
)
hwBRASQoSDropProfileWredMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredMaxThreshold.setStatus("current")


class _HwBRASQoSDropProfileWredMinThreshold_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredMinThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSDropProfileWredMinThreshold_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredMinThreshold_Object = MibTableColumn
hwBRASQoSDropProfileWredMinThreshold = _HwBRASQoSDropProfileWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 12),
    _HwBRASQoSDropProfileWredMinThreshold_Type()
)
hwBRASQoSDropProfileWredMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredMinThreshold.setStatus("current")


class _HwBRASQoSDropProfileWredGreenHighValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredGreenHighValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredGreenHighValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredGreenHighValue_Object = MibTableColumn
hwBRASQoSDropProfileWredGreenHighValue = _HwBRASQoSDropProfileWredGreenHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 13),
    _HwBRASQoSDropProfileWredGreenHighValue_Type()
)
hwBRASQoSDropProfileWredGreenHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredGreenHighValue.setStatus("current")


class _HwBRASQoSDropProfileWredGreenLowValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredGreenLowValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredGreenLowValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredGreenLowValue_Object = MibTableColumn
hwBRASQoSDropProfileWredGreenLowValue = _HwBRASQoSDropProfileWredGreenLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 14),
    _HwBRASQoSDropProfileWredGreenLowValue_Type()
)
hwBRASQoSDropProfileWredGreenLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredGreenLowValue.setStatus("current")


class _HwBRASQoSDropProfileWredGreenMaxDrop_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredGreenMaxDrop based on Integer32"""
    defaultBinValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSDropProfileWredGreenMaxDrop_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredGreenMaxDrop_Object = MibTableColumn
hwBRASQoSDropProfileWredGreenMaxDrop = _HwBRASQoSDropProfileWredGreenMaxDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 15),
    _HwBRASQoSDropProfileWredGreenMaxDrop_Type()
)
hwBRASQoSDropProfileWredGreenMaxDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredGreenMaxDrop.setStatus("current")


class _HwBRASQoSDropProfileWredYellowHighValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredYellowHighValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredYellowHighValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredYellowHighValue_Object = MibTableColumn
hwBRASQoSDropProfileWredYellowHighValue = _HwBRASQoSDropProfileWredYellowHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 16),
    _HwBRASQoSDropProfileWredYellowHighValue_Type()
)
hwBRASQoSDropProfileWredYellowHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredYellowHighValue.setStatus("current")


class _HwBRASQoSDropProfileWredYellowLowValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredYellowLowValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredYellowLowValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredYellowLowValue_Object = MibTableColumn
hwBRASQoSDropProfileWredYellowLowValue = _HwBRASQoSDropProfileWredYellowLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 17),
    _HwBRASQoSDropProfileWredYellowLowValue_Type()
)
hwBRASQoSDropProfileWredYellowLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredYellowLowValue.setStatus("current")


class _HwBRASQoSDropProfileWredYellowMaxDrop_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredYellowMaxDrop based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSDropProfileWredYellowMaxDrop_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredYellowMaxDrop_Object = MibTableColumn
hwBRASQoSDropProfileWredYellowMaxDrop = _HwBRASQoSDropProfileWredYellowMaxDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 18),
    _HwBRASQoSDropProfileWredYellowMaxDrop_Type()
)
hwBRASQoSDropProfileWredYellowMaxDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredYellowMaxDrop.setStatus("current")


class _HwBRASQoSDropProfileWredRedHighValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredRedHighValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredRedHighValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredRedHighValue_Object = MibTableColumn
hwBRASQoSDropProfileWredRedHighValue = _HwBRASQoSDropProfileWredRedHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 19),
    _HwBRASQoSDropProfileWredRedHighValue_Type()
)
hwBRASQoSDropProfileWredRedHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredRedHighValue.setStatus("current")


class _HwBRASQoSDropProfileWredRedLowValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredRedLowValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredRedLowValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredRedLowValue_Object = MibTableColumn
hwBRASQoSDropProfileWredRedLowValue = _HwBRASQoSDropProfileWredRedLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 20),
    _HwBRASQoSDropProfileWredRedLowValue_Type()
)
hwBRASQoSDropProfileWredRedLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredRedLowValue.setStatus("current")


class _HwBRASQoSDropProfileWredRedMaxDrop_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredRedMaxDrop based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSDropProfileWredRedMaxDrop_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredRedMaxDrop_Object = MibTableColumn
hwBRASQoSDropProfileWredRedMaxDrop = _HwBRASQoSDropProfileWredRedMaxDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 21),
    _HwBRASQoSDropProfileWredRedMaxDrop_Type()
)
hwBRASQoSDropProfileWredRedMaxDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredRedMaxDrop.setStatus("current")


class _HwBRASQoSDropProfileWredUserDefHighValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredUserDefHighValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredUserDefHighValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredUserDefHighValue_Object = MibTableColumn
hwBRASQoSDropProfileWredUserDefHighValue = _HwBRASQoSDropProfileWredUserDefHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 22),
    _HwBRASQoSDropProfileWredUserDefHighValue_Type()
)
hwBRASQoSDropProfileWredUserDefHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredUserDefHighValue.setStatus("current")


class _HwBRASQoSDropProfileWredUserDefLowValue_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredUserDefLowValue based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwBRASQoSDropProfileWredUserDefLowValue_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredUserDefLowValue_Object = MibTableColumn
hwBRASQoSDropProfileWredUserDefLowValue = _HwBRASQoSDropProfileWredUserDefLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 23),
    _HwBRASQoSDropProfileWredUserDefLowValue_Type()
)
hwBRASQoSDropProfileWredUserDefLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredUserDefLowValue.setStatus("current")


class _HwBRASQoSDropProfileWredUserDefMaxDrop_Type(Integer32):
    """Custom type hwBRASQoSDropProfileWredUserDefMaxDrop based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSDropProfileWredUserDefMaxDrop_Type.__name__ = "Integer32"
_HwBRASQoSDropProfileWredUserDefMaxDrop_Object = MibTableColumn
hwBRASQoSDropProfileWredUserDefMaxDrop = _HwBRASQoSDropProfileWredUserDefMaxDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 24),
    _HwBRASQoSDropProfileWredUserDefMaxDrop_Type()
)
hwBRASQoSDropProfileWredUserDefMaxDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileWredUserDefMaxDrop.setStatus("current")
_HwBRASQoSDropProfileRowStatus_Type = RowStatus
_HwBRASQoSDropProfileRowStatus_Object = MibTableColumn
hwBRASQoSDropProfileRowStatus = _HwBRASQoSDropProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 3, 1, 25),
    _HwBRASQoSDropProfileRowStatus_Type()
)
hwBRASQoSDropProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSDropProfileRowStatus.setStatus("current")
_HwBRASQoSQueueProfileTable_Object = MibTable
hwBRASQoSQueueProfileTable = _HwBRASQoSQueueProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4)
)
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileTable.setStatus("current")
_HwBRASQoSQueueProfileEntry_Object = MibTableRow
hwBRASQoSQueueProfileEntry = _HwBRASQoSQueueProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1)
)
hwBRASQoSQueueProfileEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileEntry.setStatus("current")


class _HwBRASQoSQueueProfileIndex_Type(Integer32):
    """Custom type hwBRASQoSQueueProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwBRASQoSQueueProfileIndex_Type.__name__ = "Integer32"
_HwBRASQoSQueueProfileIndex_Object = MibTableColumn
hwBRASQoSQueueProfileIndex = _HwBRASQoSQueueProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 1),
    _HwBRASQoSQueueProfileIndex_Type()
)
hwBRASQoSQueueProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileIndex.setStatus("current")


class _HwBRASQoSQueueProfileName_Type(OctetString):
    """Custom type hwBRASQoSQueueProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQueueProfileName_Type.__name__ = "OctetString"
_HwBRASQoSQueueProfileName_Object = MibTableColumn
hwBRASQoSQueueProfileName = _HwBRASQoSQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 2),
    _HwBRASQoSQueueProfileName_Type()
)
hwBRASQoSQueueProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileName.setStatus("current")


class _HwBRASQoSQueueProfileBeStyle_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileBeStyle based on SchedulerStyle"""


_HwBRASQoSQueueProfileBeStyle_Object = MibTableColumn
hwBRASQoSQueueProfileBeStyle = _HwBRASQoSQueueProfileBeStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 3),
    _HwBRASQoSQueueProfileBeStyle_Type()
)
hwBRASQoSQueueProfileBeStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileBeStyle.setStatus("current")


class _HwBRASQoSQueueProfileAf1Style_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileAf1Style based on SchedulerStyle"""


_HwBRASQoSQueueProfileAf1Style_Object = MibTableColumn
hwBRASQoSQueueProfileAf1Style = _HwBRASQoSQueueProfileAf1Style_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 4),
    _HwBRASQoSQueueProfileAf1Style_Type()
)
hwBRASQoSQueueProfileAf1Style.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileAf1Style.setStatus("current")


class _HwBRASQoSQueueProfileAf2Style_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileAf2Style based on SchedulerStyle"""


_HwBRASQoSQueueProfileAf2Style_Object = MibTableColumn
hwBRASQoSQueueProfileAf2Style = _HwBRASQoSQueueProfileAf2Style_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 5),
    _HwBRASQoSQueueProfileAf2Style_Type()
)
hwBRASQoSQueueProfileAf2Style.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileAf2Style.setStatus("current")


class _HwBRASQoSQueueProfileAf3Style_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileAf3Style based on SchedulerStyle"""


_HwBRASQoSQueueProfileAf3Style_Object = MibTableColumn
hwBRASQoSQueueProfileAf3Style = _HwBRASQoSQueueProfileAf3Style_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 6),
    _HwBRASQoSQueueProfileAf3Style_Type()
)
hwBRASQoSQueueProfileAf3Style.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileAf3Style.setStatus("current")


class _HwBRASQoSQueueProfileAf4Style_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileAf4Style based on SchedulerStyle"""


_HwBRASQoSQueueProfileAf4Style_Object = MibTableColumn
hwBRASQoSQueueProfileAf4Style = _HwBRASQoSQueueProfileAf4Style_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 7),
    _HwBRASQoSQueueProfileAf4Style_Type()
)
hwBRASQoSQueueProfileAf4Style.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileAf4Style.setStatus("current")


class _HwBRASQoSQueueProfileEfStyle_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileEfStyle based on SchedulerStyle"""


_HwBRASQoSQueueProfileEfStyle_Object = MibTableColumn
hwBRASQoSQueueProfileEfStyle = _HwBRASQoSQueueProfileEfStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 8),
    _HwBRASQoSQueueProfileEfStyle_Type()
)
hwBRASQoSQueueProfileEfStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileEfStyle.setStatus("current")


class _HwBRASQoSQueueProfileCs6Style_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileCs6Style based on SchedulerStyle"""


_HwBRASQoSQueueProfileCs6Style_Object = MibTableColumn
hwBRASQoSQueueProfileCs6Style = _HwBRASQoSQueueProfileCs6Style_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 9),
    _HwBRASQoSQueueProfileCs6Style_Type()
)
hwBRASQoSQueueProfileCs6Style.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileCs6Style.setStatus("current")


class _HwBRASQoSQueueProfileCs7Style_Type(SchedulerStyle):
    """Custom type hwBRASQoSQueueProfileCs7Style based on SchedulerStyle"""


_HwBRASQoSQueueProfileCs7Style_Object = MibTableColumn
hwBRASQoSQueueProfileCs7Style = _HwBRASQoSQueueProfileCs7Style_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 10),
    _HwBRASQoSQueueProfileCs7Style_Type()
)
hwBRASQoSQueueProfileCs7Style.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileCs7Style.setStatus("current")
_HwBRASQoSQueueProfileRowStatus_Type = RowStatus
_HwBRASQoSQueueProfileRowStatus_Object = MibTableColumn
hwBRASQoSQueueProfileRowStatus = _HwBRASQoSQueueProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 4, 1, 11),
    _HwBRASQoSQueueProfileRowStatus_Type()
)
hwBRASQoSQueueProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSQueueProfileRowStatus.setStatus("current")
_HwBRASQoSQueueClassTable_Object = MibTable
hwBRASQoSQueueClassTable = _HwBRASQoSQueueClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5)
)
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassTable.setStatus("current")
_HwBRASQoSQueueClassEntry_Object = MibTableRow
hwBRASQoSQueueClassEntry = _HwBRASQoSQueueClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1)
)
hwBRASQoSQueueClassEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassProfileName"),
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassServiceId"),
)
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassEntry.setStatus("current")


class _HwBRASQoSQueueClassProfileName_Type(OctetString):
    """Custom type hwBRASQoSQueueClassProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQueueClassProfileName_Type.__name__ = "OctetString"
_HwBRASQoSQueueClassProfileName_Object = MibTableColumn
hwBRASQoSQueueClassProfileName = _HwBRASQoSQueueClassProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 1),
    _HwBRASQoSQueueClassProfileName_Type()
)
hwBRASQoSQueueClassProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassProfileName.setStatus("current")
_HwBRASQoSQueueClassServiceId_Type = QueueClass
_HwBRASQoSQueueClassServiceId_Object = MibTableColumn
hwBRASQoSQueueClassServiceId = _HwBRASQoSQueueClassServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 2),
    _HwBRASQoSQueueClassServiceId_Type()
)
hwBRASQoSQueueClassServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassServiceId.setStatus("current")


class _HwBRASQoSQueueClassWredEnableStatus_Type(TruthValue):
    """Custom type hwBRASQoSQueueClassWredEnableStatus based on TruthValue"""


_HwBRASQoSQueueClassWredEnableStatus_Object = MibTableColumn
hwBRASQoSQueueClassWredEnableStatus = _HwBRASQoSQueueClassWredEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 3),
    _HwBRASQoSQueueClassWredEnableStatus_Type()
)
hwBRASQoSQueueClassWredEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassWredEnableStatus.setStatus("current")


class _HwBRASQoSQueueClassWredWeight_Type(Integer32):
    """Custom type hwBRASQoSQueueClassWredWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwBRASQoSQueueClassWredWeight_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassWredWeight_Object = MibTableColumn
hwBRASQoSQueueClassWredWeight = _HwBRASQoSQueueClassWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 4),
    _HwBRASQoSQueueClassWredWeight_Type()
)
hwBRASQoSQueueClassWredWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassWredWeight.setStatus("current")


class _HwBRASQoSQueueClassWrrWeight_Type(Integer32):
    """Custom type hwBRASQoSQueueClassWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwBRASQoSQueueClassWrrWeight_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassWrrWeight_Object = MibTableColumn
hwBRASQoSQueueClassWrrWeight = _HwBRASQoSQueueClassWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 5),
    _HwBRASQoSQueueClassWrrWeight_Type()
)
hwBRASQoSQueueClassWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassWrrWeight.setStatus("current")


class _HwBRASQoSQueueClassLength_Type(Integer32):
    """Custom type hwBRASQoSQueueClassLength based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 64),
    )


_HwBRASQoSQueueClassLength_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassLength_Object = MibTableColumn
hwBRASQoSQueueClassLength = _HwBRASQoSQueueClassLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 6),
    _HwBRASQoSQueueClassLength_Type()
)
hwBRASQoSQueueClassLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassLength.setStatus("current")


class _HwBRASQoSQueueClassCir_Type(Integer32):
    """Custom type hwBRASQoSQueueClassCir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(100, 3000000),
    )


_HwBRASQoSQueueClassCir_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassCir_Object = MibTableColumn
hwBRASQoSQueueClassCir = _HwBRASQoSQueueClassCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 7),
    _HwBRASQoSQueueClassCir_Type()
)
hwBRASQoSQueueClassCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassCir.setStatus("current")


class _HwBRASQoSQueueClassCbs_Type(Integer32):
    """Custom type hwBRASQoSQueueClassCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(64, 131071),
    )


_HwBRASQoSQueueClassCbs_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassCbs_Object = MibTableColumn
hwBRASQoSQueueClassCbs = _HwBRASQoSQueueClassCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 8),
    _HwBRASQoSQueueClassCbs_Type()
)
hwBRASQoSQueueClassCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassCbs.setStatus("current")


class _HwBRASQoSQueueClassPir_Type(Integer32):
    """Custom type hwBRASQoSQueueClassPir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(100, 3000000),
    )


_HwBRASQoSQueueClassPir_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassPir_Object = MibTableColumn
hwBRASQoSQueueClassPir = _HwBRASQoSQueueClassPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 9),
    _HwBRASQoSQueueClassPir_Type()
)
hwBRASQoSQueueClassPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassPir.setStatus("current")


class _HwBRASQoSQueueClassPbs_Type(Integer32):
    """Custom type hwBRASQoSQueueClassPbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(64, 4000000),
    )


_HwBRASQoSQueueClassPbs_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassPbs_Object = MibTableColumn
hwBRASQoSQueueClassPbs = _HwBRASQoSQueueClassPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 10),
    _HwBRASQoSQueueClassPbs_Type()
)
hwBRASQoSQueueClassPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassPbs.setStatus("current")


class _HwBRASQoSQueueClassWfqWeight_Type(Integer32):
    """Custom type hwBRASQoSQueueClassWfqWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSQueueClassWfqWeight_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassWfqWeight_Object = MibTableColumn
hwBRASQoSQueueClassWfqWeight = _HwBRASQoSQueueClassWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 11),
    _HwBRASQoSQueueClassWfqWeight_Type()
)
hwBRASQoSQueueClassWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassWfqWeight.setStatus("current")


class _HwBRASQoSQueueClassShaping_Type(Integer32):
    """Custom type hwBRASQoSQueueClassShaping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSQueueClassShaping_Type.__name__ = "Integer32"
_HwBRASQoSQueueClassShaping_Object = MibTableColumn
hwBRASQoSQueueClassShaping = _HwBRASQoSQueueClassShaping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 12),
    _HwBRASQoSQueueClassShaping_Type()
)
hwBRASQoSQueueClassShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassShaping.setStatus("current")
_HwBRASQoSQueueClassScheduler_Type = SchedulerService
_HwBRASQoSQueueClassScheduler_Object = MibTableColumn
hwBRASQoSQueueClassScheduler = _HwBRASQoSQueueClassScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 13),
    _HwBRASQoSQueueClassScheduler_Type()
)
hwBRASQoSQueueClassScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassScheduler.setStatus("current")


class _HwBRASQoSQueueClassDropName_Type(OctetString):
    """Custom type hwBRASQoSQueueClassDropName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSQueueClassDropName_Type.__name__ = "OctetString"
_HwBRASQoSQueueClassDropName_Object = MibTableColumn
hwBRASQoSQueueClassDropName = _HwBRASQoSQueueClassDropName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 5, 1, 14),
    _HwBRASQoSQueueClassDropName_Type()
)
hwBRASQoSQueueClassDropName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSQueueClassDropName.setStatus("current")
_HwBRASQoSFlowMappingTable_Object = MibTable
hwBRASQoSFlowMappingTable = _HwBRASQoSFlowMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6)
)
if mibBuilder.loadTexts:
    hwBRASQoSFlowMappingTable.setStatus("current")
_HwBRASQoSFlowMappingEntry_Object = MibTableRow
hwBRASQoSFlowMappingEntry = _HwBRASQoSFlowMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1)
)
hwBRASQoSFlowMappingEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSFlowMappingName"),
)
if mibBuilder.loadTexts:
    hwBRASQoSFlowMappingEntry.setStatus("current")


class _HwBRASQoSFlowMappingName_Type(OctetString):
    """Custom type hwBRASQoSFlowMappingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSFlowMappingName_Type.__name__ = "OctetString"
_HwBRASQoSFlowMappingName_Object = MibTableColumn
hwBRASQoSFlowMappingName = _HwBRASQoSFlowMappingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 1),
    _HwBRASQoSFlowMappingName_Type()
)
hwBRASQoSFlowMappingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSFlowMappingName.setStatus("current")


class _HwBRASQoSBeMapping_Type(QueueClass):
    """Custom type hwBRASQoSBeMapping based on QueueClass"""


_HwBRASQoSBeMapping_Object = MibTableColumn
hwBRASQoSBeMapping = _HwBRASQoSBeMapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 2),
    _HwBRASQoSBeMapping_Type()
)
hwBRASQoSBeMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSBeMapping.setStatus("current")


class _HwBRASQoSAf1Mapping_Type(QueueClass):
    """Custom type hwBRASQoSAf1Mapping based on QueueClass"""


_HwBRASQoSAf1Mapping_Object = MibTableColumn
hwBRASQoSAf1Mapping = _HwBRASQoSAf1Mapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 3),
    _HwBRASQoSAf1Mapping_Type()
)
hwBRASQoSAf1Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSAf1Mapping.setStatus("current")


class _HwBRASQoSAf2Mapping_Type(QueueClass):
    """Custom type hwBRASQoSAf2Mapping based on QueueClass"""


_HwBRASQoSAf2Mapping_Object = MibTableColumn
hwBRASQoSAf2Mapping = _HwBRASQoSAf2Mapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 4),
    _HwBRASQoSAf2Mapping_Type()
)
hwBRASQoSAf2Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSAf2Mapping.setStatus("current")


class _HwBRASQoSAf3Mapping_Type(QueueClass):
    """Custom type hwBRASQoSAf3Mapping based on QueueClass"""


_HwBRASQoSAf3Mapping_Object = MibTableColumn
hwBRASQoSAf3Mapping = _HwBRASQoSAf3Mapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 5),
    _HwBRASQoSAf3Mapping_Type()
)
hwBRASQoSAf3Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSAf3Mapping.setStatus("current")


class _HwBRASQoSAf4Mapping_Type(QueueClass):
    """Custom type hwBRASQoSAf4Mapping based on QueueClass"""


_HwBRASQoSAf4Mapping_Object = MibTableColumn
hwBRASQoSAf4Mapping = _HwBRASQoSAf4Mapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 6),
    _HwBRASQoSAf4Mapping_Type()
)
hwBRASQoSAf4Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSAf4Mapping.setStatus("current")


class _HwBRASQoSEfMapping_Type(QueueClass):
    """Custom type hwBRASQoSEfMapping based on QueueClass"""


_HwBRASQoSEfMapping_Object = MibTableColumn
hwBRASQoSEfMapping = _HwBRASQoSEfMapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 7),
    _HwBRASQoSEfMapping_Type()
)
hwBRASQoSEfMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSEfMapping.setStatus("current")


class _HwBRASQoSCs6Mapping_Type(QueueClass):
    """Custom type hwBRASQoSCs6Mapping based on QueueClass"""


_HwBRASQoSCs6Mapping_Object = MibTableColumn
hwBRASQoSCs6Mapping = _HwBRASQoSCs6Mapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 8),
    _HwBRASQoSCs6Mapping_Type()
)
hwBRASQoSCs6Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCs6Mapping.setStatus("current")


class _HwBRASQoSCs7Mapping_Type(QueueClass):
    """Custom type hwBRASQoSCs7Mapping based on QueueClass"""


_HwBRASQoSCs7Mapping_Object = MibTableColumn
hwBRASQoSCs7Mapping = _HwBRASQoSCs7Mapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 9),
    _HwBRASQoSCs7Mapping_Type()
)
hwBRASQoSCs7Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCs7Mapping.setStatus("current")
_HwBRASQoSFlowMappingRowStatus_Type = RowStatus
_HwBRASQoSFlowMappingRowStatus_Object = MibTableColumn
hwBRASQoSFlowMappingRowStatus = _HwBRASQoSFlowMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 6, 1, 10),
    _HwBRASQoSFlowMappingRowStatus_Type()
)
hwBRASQoSFlowMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSFlowMappingRowStatus.setStatus("current")
_HwBRASQoSIfTable_Object = MibTable
hwBRASQoSIfTable = _HwBRASQoSIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7)
)
if mibBuilder.loadTexts:
    hwBRASQoSIfTable.setStatus("current")
_HwBRASQoSIfEntry_Object = MibTableRow
hwBRASQoSIfEntry = _HwBRASQoSIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1)
)
hwBRASQoSIfEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSIfEntry.setStatus("current")
_HwBRASQoSIfIndex_Type = InterfaceIndex
_HwBRASQoSIfIndex_Object = MibTableColumn
hwBRASQoSIfIndex = _HwBRASQoSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 1),
    _HwBRASQoSIfIndex_Type()
)
hwBRASQoSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSIfIndex.setStatus("current")


class _HwBRASQoSIfName_Type(OctetString):
    """Custom type hwBRASQoSIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBRASQoSIfName_Type.__name__ = "OctetString"
_HwBRASQoSIfName_Object = MibTableColumn
hwBRASQoSIfName = _HwBRASQoSIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 2),
    _HwBRASQoSIfName_Type()
)
hwBRASQoSIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSIfName.setStatus("current")


class _HwBRASQoSIfQoSProfileName_Type(OctetString):
    """Custom type hwBRASQoSIfQoSProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfQoSProfileName_Type.__name__ = "OctetString"
_HwBRASQoSIfQoSProfileName_Object = MibTableColumn
hwBRASQoSIfQoSProfileName = _HwBRASQoSIfQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 3),
    _HwBRASQoSIfQoSProfileName_Type()
)
hwBRASQoSIfQoSProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfQoSProfileName.setStatus("current")
_HwBRASQoSIfScheduleId_Type = InterfaceScheduler
_HwBRASQoSIfScheduleId_Object = MibTableColumn
hwBRASQoSIfScheduleId = _HwBRASQoSIfScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 4),
    _HwBRASQoSIfScheduleId_Type()
)
hwBRASQoSIfScheduleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfScheduleId.setStatus("current")


class _HwBRASQoSIfServiceGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfServiceGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfServiceGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfServiceGroupName_Object = MibTableColumn
hwBRASQoSIfServiceGroupName = _HwBRASQoSIfServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 5),
    _HwBRASQoSIfServiceGroupName_Type()
)
hwBRASQoSIfServiceGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfServiceGroupName.setStatus("current")


class _HwBRASQoSIfShapingValue_Type(Integer32):
    """Custom type hwBRASQoSIfShapingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HwBRASQoSIfShapingValue_Type.__name__ = "Integer32"
_HwBRASQoSIfShapingValue_Object = MibTableColumn
hwBRASQoSIfShapingValue = _HwBRASQoSIfShapingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 6),
    _HwBRASQoSIfShapingValue_Type()
)
hwBRASQoSIfShapingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfShapingValue.setStatus("current")


class _HwBRASQoSIfVpGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfVpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfVpGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfVpGroupName_Object = MibTableColumn
hwBRASQoSIfVpGroupName = _HwBRASQoSIfVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 7),
    _HwBRASQoSIfVpGroupName_Type()
)
hwBRASQoSIfVpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVpGroupName.setStatus("current")


class _HwBRASQoSIfInboundVcGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfInboundVcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfInboundVcGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfInboundVcGroupName_Object = MibTableColumn
hwBRASQoSIfInboundVcGroupName = _HwBRASQoSIfInboundVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 8),
    _HwBRASQoSIfInboundVcGroupName_Type()
)
hwBRASQoSIfInboundVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfInboundVcGroupName.setStatus("current")


class _HwBRASQoSIfOutboundAVcGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfOutboundAVcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfOutboundAVcGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfOutboundAVcGroupName_Object = MibTableColumn
hwBRASQoSIfOutboundAVcGroupName = _HwBRASQoSIfOutboundAVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 9),
    _HwBRASQoSIfOutboundAVcGroupName_Type()
)
hwBRASQoSIfOutboundAVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfOutboundAVcGroupName.setStatus("current")


class _HwBRASQoSIfOutboundBVcGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfOutboundBVcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfOutboundBVcGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfOutboundBVcGroupName_Object = MibTableColumn
hwBRASQoSIfOutboundBVcGroupName = _HwBRASQoSIfOutboundBVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 10),
    _HwBRASQoSIfOutboundBVcGroupName_Type()
)
hwBRASQoSIfOutboundBVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfOutboundBVcGroupName.setStatus("current")


class _HwBRASQoSIfInboundGVpGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfInboundGVpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfInboundGVpGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfInboundGVpGroupName_Object = MibTableColumn
hwBRASQoSIfInboundGVpGroupName = _HwBRASQoSIfInboundGVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 11),
    _HwBRASQoSIfInboundGVpGroupName_Type()
)
hwBRASQoSIfInboundGVpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfInboundGVpGroupName.setStatus("current")


class _HwBRASQoSIfOutboundAGVpGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfOutboundAGVpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfOutboundAGVpGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfOutboundAGVpGroupName_Object = MibTableColumn
hwBRASQoSIfOutboundAGVpGroupName = _HwBRASQoSIfOutboundAGVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 12),
    _HwBRASQoSIfOutboundAGVpGroupName_Type()
)
hwBRASQoSIfOutboundAGVpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfOutboundAGVpGroupName.setStatus("current")


class _HwBRASQoSIfPacketAjustOverhead_Type(Integer32):
    """Custom type hwBRASQoSIfPacketAjustOverhead based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-34, 34),
    )


_HwBRASQoSIfPacketAjustOverhead_Type.__name__ = "Integer32"
_HwBRASQoSIfPacketAjustOverhead_Object = MibTableColumn
hwBRASQoSIfPacketAjustOverhead = _HwBRASQoSIfPacketAjustOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 13),
    _HwBRASQoSIfPacketAjustOverhead_Type()
)
hwBRASQoSIfPacketAjustOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfPacketAjustOverhead.setStatus("current")


class _HwBRASQoSIfRemoteLinkMode_Type(LinkMode):
    """Custom type hwBRASQoSIfRemoteLinkMode based on LinkMode"""


_HwBRASQoSIfRemoteLinkMode_Object = MibTableColumn
hwBRASQoSIfRemoteLinkMode = _HwBRASQoSIfRemoteLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 14),
    _HwBRASQoSIfRemoteLinkMode_Type()
)
hwBRASQoSIfRemoteLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfRemoteLinkMode.setStatus("current")


class _HwBRASQoSIfInCarProfileName_Type(OctetString):
    """Custom type hwBRASQoSIfInCarProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfInCarProfileName_Type.__name__ = "OctetString"
_HwBRASQoSIfInCarProfileName_Object = MibTableColumn
hwBRASQoSIfInCarProfileName = _HwBRASQoSIfInCarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 15),
    _HwBRASQoSIfInCarProfileName_Type()
)
hwBRASQoSIfInCarProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfInCarProfileName.setStatus("current")


class _HwBRASQoSIfInStatistics_Type(StatMode):
    """Custom type hwBRASQoSIfInStatistics based on StatMode"""


_HwBRASQoSIfInStatistics_Object = MibTableColumn
hwBRASQoSIfInStatistics = _HwBRASQoSIfInStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 16),
    _HwBRASQoSIfInStatistics_Type()
)
hwBRASQoSIfInStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfInStatistics.setStatus("current")


class _HwBRASQoSIfOutCarProfileName_Type(OctetString):
    """Custom type hwBRASQoSIfOutCarProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfOutCarProfileName_Type.__name__ = "OctetString"
_HwBRASQoSIfOutCarProfileName_Object = MibTableColumn
hwBRASQoSIfOutCarProfileName = _HwBRASQoSIfOutCarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 17),
    _HwBRASQoSIfOutCarProfileName_Type()
)
hwBRASQoSIfOutCarProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfOutCarProfileName.setStatus("current")


class _HwBRASQoSIfOutStatistics_Type(StatMode):
    """Custom type hwBRASQoSIfOutStatistics based on StatMode"""


_HwBRASQoSIfOutStatistics_Object = MibTableColumn
hwBRASQoSIfOutStatistics = _HwBRASQoSIfOutStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 18),
    _HwBRASQoSIfOutStatistics_Type()
)
hwBRASQoSIfOutStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfOutStatistics.setStatus("current")


class _HwBRASQoSIfVplsCarStatus_Type(TruthValue):
    """Custom type hwBRASQoSIfVplsCarStatus based on TruthValue"""


_HwBRASQoSIfVplsCarStatus_Object = MibTableColumn
hwBRASQoSIfVplsCarStatus = _HwBRASQoSIfVplsCarStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 19),
    _HwBRASQoSIfVplsCarStatus_Type()
)
hwBRASQoSIfVplsCarStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVplsCarStatus.setStatus("current")


class _HwBRASQoSIfMultiShapingStatus_Type(TruthValue):
    """Custom type hwBRASQoSIfMultiShapingStatus based on TruthValue"""


_HwBRASQoSIfMultiShapingStatus_Object = MibTableColumn
hwBRASQoSIfMultiShapingStatus = _HwBRASQoSIfMultiShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 20),
    _HwBRASQoSIfMultiShapingStatus_Type()
)
hwBRASQoSIfMultiShapingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfMultiShapingStatus.setStatus("current")
_HwBRASQoSIfActiveStatus_Type = TruthValue
_HwBRASQoSIfActiveStatus_Object = MibTableColumn
hwBRASQoSIfActiveStatus = _HwBRASQoSIfActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 7, 1, 21),
    _HwBRASQoSIfActiveStatus_Type()
)
hwBRASQoSIfActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSIfActiveStatus.setStatus("current")
_HwBRASQoSIfVcTable_Object = MibTable
hwBRASQoSIfVcTable = _HwBRASQoSIfVcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8)
)
if mibBuilder.loadTexts:
    hwBRASQoSIfVcTable.setStatus("current")
_HwBRASQoSIfVcEntry_Object = MibTableRow
hwBRASQoSIfVcEntry = _HwBRASQoSIfVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1)
)
hwBRASQoSIfVcEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcIfIndex"),
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcVlanId"),
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcQinqVlanId"),
)
if mibBuilder.loadTexts:
    hwBRASQoSIfVcEntry.setStatus("current")
_HwBRASQoSIfVcIfIndex_Type = InterfaceIndex
_HwBRASQoSIfVcIfIndex_Object = MibTableColumn
hwBRASQoSIfVcIfIndex = _HwBRASQoSIfVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 1),
    _HwBRASQoSIfVcIfIndex_Type()
)
hwBRASQoSIfVcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcIfIndex.setStatus("current")


class _HwBRASQoSIfVcVlanId_Type(VlanIndex):
    """Custom type hwBRASQoSIfVcVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwBRASQoSIfVcVlanId_Type.__name__ = "VlanIndex"
_HwBRASQoSIfVcVlanId_Object = MibTableColumn
hwBRASQoSIfVcVlanId = _HwBRASQoSIfVcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 2),
    _HwBRASQoSIfVcVlanId_Type()
)
hwBRASQoSIfVcVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcVlanId.setStatus("current")


class _HwBRASQoSIfVcQinqVlanId_Type(VlanIndex):
    """Custom type hwBRASQoSIfVcQinqVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwBRASQoSIfVcQinqVlanId_Type.__name__ = "VlanIndex"
_HwBRASQoSIfVcQinqVlanId_Object = MibTableColumn
hwBRASQoSIfVcQinqVlanId = _HwBRASQoSIfVcQinqVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 3),
    _HwBRASQoSIfVcQinqVlanId_Type()
)
hwBRASQoSIfVcQinqVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcQinqVlanId.setStatus("current")


class _HwBRASQoSIfVcVlanEndId_Type(VlanIndex):
    """Custom type hwBRASQoSIfVcVlanEndId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_HwBRASQoSIfVcVlanEndId_Type.__name__ = "VlanIndex"
_HwBRASQoSIfVcVlanEndId_Object = MibTableColumn
hwBRASQoSIfVcVlanEndId = _HwBRASQoSIfVcVlanEndId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 4),
    _HwBRASQoSIfVcVlanEndId_Type()
)
hwBRASQoSIfVcVlanEndId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcVlanEndId.setStatus("current")


class _HwBRASQoSIfVcQinqVlanEndId_Type(VlanIndex):
    """Custom type hwBRASQoSIfVcQinqVlanEndId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_HwBRASQoSIfVcQinqVlanEndId_Type.__name__ = "VlanIndex"
_HwBRASQoSIfVcQinqVlanEndId_Object = MibTableColumn
hwBRASQoSIfVcQinqVlanEndId = _HwBRASQoSIfVcQinqVlanEndId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 5),
    _HwBRASQoSIfVcQinqVlanEndId_Type()
)
hwBRASQoSIfVcQinqVlanEndId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcQinqVlanEndId.setStatus("current")


class _HwBRASQoSIfVcVcGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfVcVcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBRASQoSIfVcVcGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfVcVcGroupName_Object = MibTableColumn
hwBRASQoSIfVcVcGroupName = _HwBRASQoSIfVcVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 6),
    _HwBRASQoSIfVcVcGroupName_Type()
)
hwBRASQoSIfVcVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcVcGroupName.setStatus("current")


class _HwBRASQoSIfVcServiceGroupName_Type(OctetString):
    """Custom type hwBRASQoSIfVcServiceGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBRASQoSIfVcServiceGroupName_Type.__name__ = "OctetString"
_HwBRASQoSIfVcServiceGroupName_Object = MibTableColumn
hwBRASQoSIfVcServiceGroupName = _HwBRASQoSIfVcServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 7),
    _HwBRASQoSIfVcServiceGroupName_Type()
)
hwBRASQoSIfVcServiceGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcServiceGroupName.setStatus("current")


class _HwBRASQoSIfVcInCarProfileName_Type(OctetString):
    """Custom type hwBRASQoSIfVcInCarProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfVcInCarProfileName_Type.__name__ = "OctetString"
_HwBRASQoSIfVcInCarProfileName_Object = MibTableColumn
hwBRASQoSIfVcInCarProfileName = _HwBRASQoSIfVcInCarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 8),
    _HwBRASQoSIfVcInCarProfileName_Type()
)
hwBRASQoSIfVcInCarProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcInCarProfileName.setStatus("current")


class _HwBRASQoSIfVcInStatistics_Type(StatMode):
    """Custom type hwBRASQoSIfVcInStatistics based on StatMode"""


_HwBRASQoSIfVcInStatistics_Object = MibTableColumn
hwBRASQoSIfVcInStatistics = _HwBRASQoSIfVcInStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 9),
    _HwBRASQoSIfVcInStatistics_Type()
)
hwBRASQoSIfVcInStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcInStatistics.setStatus("current")


class _HwBRASQoSIfVcInCarEachVlanStatus_Type(TruthValue):
    """Custom type hwBRASQoSIfVcInCarEachVlanStatus based on TruthValue"""


_HwBRASQoSIfVcInCarEachVlanStatus_Object = MibTableColumn
hwBRASQoSIfVcInCarEachVlanStatus = _HwBRASQoSIfVcInCarEachVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 10),
    _HwBRASQoSIfVcInCarEachVlanStatus_Type()
)
hwBRASQoSIfVcInCarEachVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcInCarEachVlanStatus.setStatus("current")


class _HwBRASQoSIfVcOutCarProfileName_Type(OctetString):
    """Custom type hwBRASQoSIfVcOutCarProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSIfVcOutCarProfileName_Type.__name__ = "OctetString"
_HwBRASQoSIfVcOutCarProfileName_Object = MibTableColumn
hwBRASQoSIfVcOutCarProfileName = _HwBRASQoSIfVcOutCarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 11),
    _HwBRASQoSIfVcOutCarProfileName_Type()
)
hwBRASQoSIfVcOutCarProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcOutCarProfileName.setStatus("current")


class _HwBRASQoSIfVcOutStatistics_Type(StatMode):
    """Custom type hwBRASQoSIfVcOutStatistics based on StatMode"""


_HwBRASQoSIfVcOutStatistics_Object = MibTableColumn
hwBRASQoSIfVcOutStatistics = _HwBRASQoSIfVcOutStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 12),
    _HwBRASQoSIfVcOutStatistics_Type()
)
hwBRASQoSIfVcOutStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcOutStatistics.setStatus("current")


class _HwBRASQoSIfVcOutCarEachVlanStatus_Type(TruthValue):
    """Custom type hwBRASQoSIfVcOutCarEachVlanStatus based on TruthValue"""


_HwBRASQoSIfVcOutCarEachVlanStatus_Object = MibTableColumn
hwBRASQoSIfVcOutCarEachVlanStatus = _HwBRASQoSIfVcOutCarEachVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 8, 1, 13),
    _HwBRASQoSIfVcOutCarEachVlanStatus_Type()
)
hwBRASQoSIfVcOutCarEachVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSIfVcOutCarEachVlanStatus.setStatus("current")
_HwBRASQoSVpGroupTable_Object = MibTable
hwBRASQoSVpGroupTable = _HwBRASQoSVpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 9)
)
if mibBuilder.loadTexts:
    hwBRASQoSVpGroupTable.setStatus("current")
_HwBRASQoSVpGroupEntry_Object = MibTableRow
hwBRASQoSVpGroupEntry = _HwBRASQoSVpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 9, 1)
)
hwBRASQoSVpGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupIfIndex"),
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupName"),
)
if mibBuilder.loadTexts:
    hwBRASQoSVpGroupEntry.setStatus("current")
_HwBRASQoSVpGroupIfIndex_Type = Unsigned32
_HwBRASQoSVpGroupIfIndex_Object = MibTableColumn
hwBRASQoSVpGroupIfIndex = _HwBRASQoSVpGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 9, 1, 1),
    _HwBRASQoSVpGroupIfIndex_Type()
)
hwBRASQoSVpGroupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSVpGroupIfIndex.setStatus("current")


class _HwBRASQoSVpGroupName_Type(OctetString):
    """Custom type hwBRASQoSVpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSVpGroupName_Type.__name__ = "OctetString"
_HwBRASQoSVpGroupName_Object = MibTableColumn
hwBRASQoSVpGroupName = _HwBRASQoSVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 9, 1, 2),
    _HwBRASQoSVpGroupName_Type()
)
hwBRASQoSVpGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVpGroupName.setStatus("current")


class _HwBRASQoSVpGroupQosProfileName_Type(OctetString):
    """Custom type hwBRASQoSVpGroupQosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSVpGroupQosProfileName_Type.__name__ = "OctetString"
_HwBRASQoSVpGroupQosProfileName_Object = MibTableColumn
hwBRASQoSVpGroupQosProfileName = _HwBRASQoSVpGroupQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 9, 1, 3),
    _HwBRASQoSVpGroupQosProfileName_Type()
)
hwBRASQoSVpGroupQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVpGroupQosProfileName.setStatus("current")
_HwBRASQoSVpGroupRowStatus_Type = RowStatus
_HwBRASQoSVpGroupRowStatus_Object = MibTableColumn
hwBRASQoSVpGroupRowStatus = _HwBRASQoSVpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 9, 1, 4),
    _HwBRASQoSVpGroupRowStatus_Type()
)
hwBRASQoSVpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVpGroupRowStatus.setStatus("current")
_HwBRASQoSVcGroupTable_Object = MibTable
hwBRASQoSVcGroupTable = _HwBRASQoSVcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 10)
)
if mibBuilder.loadTexts:
    hwBRASQoSVcGroupTable.setStatus("current")
_HwBRASQoSVcGroupEntry_Object = MibTableRow
hwBRASQoSVcGroupEntry = _HwBRASQoSVcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 10, 1)
)
hwBRASQoSVcGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVcGroupIfIndex"),
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVcGroupName"),
)
if mibBuilder.loadTexts:
    hwBRASQoSVcGroupEntry.setStatus("current")
_HwBRASQoSVcGroupIfIndex_Type = Unsigned32
_HwBRASQoSVcGroupIfIndex_Object = MibTableColumn
hwBRASQoSVcGroupIfIndex = _HwBRASQoSVcGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 10, 1, 1),
    _HwBRASQoSVcGroupIfIndex_Type()
)
hwBRASQoSVcGroupIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVcGroupIfIndex.setStatus("current")


class _HwBRASQoSVcGroupName_Type(OctetString):
    """Custom type hwBRASQoSVcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSVcGroupName_Type.__name__ = "OctetString"
_HwBRASQoSVcGroupName_Object = MibTableColumn
hwBRASQoSVcGroupName = _HwBRASQoSVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 10, 1, 2),
    _HwBRASQoSVcGroupName_Type()
)
hwBRASQoSVcGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVcGroupName.setStatus("current")


class _HwBRASQoSVcGroupQosProfileName_Type(OctetString):
    """Custom type hwBRASQoSVcGroupQosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSVcGroupQosProfileName_Type.__name__ = "OctetString"
_HwBRASQoSVcGroupQosProfileName_Object = MibTableColumn
hwBRASQoSVcGroupQosProfileName = _HwBRASQoSVcGroupQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 10, 1, 3),
    _HwBRASQoSVcGroupQosProfileName_Type()
)
hwBRASQoSVcGroupQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVcGroupQosProfileName.setStatus("current")
_HwBRASQoSVcGroupRowStatus_Type = RowStatus
_HwBRASQoSVcGroupRowStatus_Object = MibTableColumn
hwBRASQoSVcGroupRowStatus = _HwBRASQoSVcGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 10, 1, 4),
    _HwBRASQoSVcGroupRowStatus_Type()
)
hwBRASQoSVcGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSVcGroupRowStatus.setStatus("current")
_HwBRASQoSGVpGroupTable_Object = MibTable
hwBRASQoSGVpGroupTable = _HwBRASQoSGVpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 11)
)
if mibBuilder.loadTexts:
    hwBRASQoSGVpGroupTable.setStatus("current")
_HwBRASQoSGVpGroupEntry_Object = MibTableRow
hwBRASQoSGVpGroupEntry = _HwBRASQoSGVpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 11, 1)
)
hwBRASQoSGVpGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupName"),
)
if mibBuilder.loadTexts:
    hwBRASQoSGVpGroupEntry.setStatus("current")


class _HwBRASQoSGVpGroupSlotId_Type(Integer32):
    """Custom type hwBRASQoSGVpGroupSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBRASQoSGVpGroupSlotId_Type.__name__ = "Integer32"
_HwBRASQoSGVpGroupSlotId_Object = MibTableColumn
hwBRASQoSGVpGroupSlotId = _HwBRASQoSGVpGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 11, 1, 1),
    _HwBRASQoSGVpGroupSlotId_Type()
)
hwBRASQoSGVpGroupSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSGVpGroupSlotId.setStatus("current")


class _HwBRASQoSGVpGroupName_Type(OctetString):
    """Custom type hwBRASQoSGVpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSGVpGroupName_Type.__name__ = "OctetString"
_HwBRASQoSGVpGroupName_Object = MibTableColumn
hwBRASQoSGVpGroupName = _HwBRASQoSGVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 11, 1, 2),
    _HwBRASQoSGVpGroupName_Type()
)
hwBRASQoSGVpGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSGVpGroupName.setStatus("current")


class _HwBRASQoSGVpGroupQosProfileName_Type(OctetString):
    """Custom type hwBRASQoSGVpGroupQosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSGVpGroupQosProfileName_Type.__name__ = "OctetString"
_HwBRASQoSGVpGroupQosProfileName_Object = MibTableColumn
hwBRASQoSGVpGroupQosProfileName = _HwBRASQoSGVpGroupQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 11, 1, 3),
    _HwBRASQoSGVpGroupQosProfileName_Type()
)
hwBRASQoSGVpGroupQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSGVpGroupQosProfileName.setStatus("current")
_HwBRASQoSGVpGroupRowStatus_Type = RowStatus
_HwBRASQoSGVpGroupRowStatus_Object = MibTableColumn
hwBRASQoSGVpGroupRowStatus = _HwBRASQoSGVpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 11, 1, 4),
    _HwBRASQoSGVpGroupRowStatus_Type()
)
hwBRASQoSGVpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSGVpGroupRowStatus.setStatus("current")
_HwBRASQoSServiceGroupTable_Object = MibTable
hwBRASQoSServiceGroupTable = _HwBRASQoSServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 12)
)
if mibBuilder.loadTexts:
    hwBRASQoSServiceGroupTable.setStatus("current")
_HwBRASQoSServiceGroupEntry_Object = MibTableRow
hwBRASQoSServiceGroupEntry = _HwBRASQoSServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 12, 1)
)
hwBRASQoSServiceGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSServiceGroupIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSServiceGroupEntry.setStatus("current")


class _HwBRASQoSServiceGroupIndex_Type(Integer32):
    """Custom type hwBRASQoSServiceGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_HwBRASQoSServiceGroupIndex_Type.__name__ = "Integer32"
_HwBRASQoSServiceGroupIndex_Object = MibTableColumn
hwBRASQoSServiceGroupIndex = _HwBRASQoSServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 12, 1, 1),
    _HwBRASQoSServiceGroupIndex_Type()
)
hwBRASQoSServiceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSServiceGroupIndex.setStatus("current")


class _HwBRASQoSServiceGroupName_Type(OctetString):
    """Custom type hwBRASQoSServiceGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSServiceGroupName_Type.__name__ = "OctetString"
_HwBRASQoSServiceGroupName_Object = MibTableColumn
hwBRASQoSServiceGroupName = _HwBRASQoSServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 12, 1, 2),
    _HwBRASQoSServiceGroupName_Type()
)
hwBRASQoSServiceGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSServiceGroupName.setStatus("current")
_HwBRASQoSServiceGroupRowStatus_Type = RowStatus
_HwBRASQoSServiceGroupRowStatus_Object = MibTableColumn
hwBRASQoSServiceGroupRowStatus = _HwBRASQoSServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 12, 1, 4),
    _HwBRASQoSServiceGroupRowStatus_Type()
)
hwBRASQoSServiceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSServiceGroupRowStatus.setStatus("current")
_HwBRASQoSPortQueueTable_Object = MibTable
hwBRASQoSPortQueueTable = _HwBRASQoSPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13)
)
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueTable.setStatus("current")
_HwBRASQoSPortQueueEntry_Object = MibTableRow
hwBRASQoSPortQueueEntry = _HwBRASQoSPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1)
)
hwBRASQoSPortQueueEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueIfIndex"),
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueServiceId"),
)
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueEntry.setStatus("current")
_HwBRASQoSPortQueueIfIndex_Type = Unsigned32
_HwBRASQoSPortQueueIfIndex_Object = MibTableColumn
hwBRASQoSPortQueueIfIndex = _HwBRASQoSPortQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 1),
    _HwBRASQoSPortQueueIfIndex_Type()
)
hwBRASQoSPortQueueIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueIfIndex.setStatus("current")
_HwBRASQoSPortQueueServiceId_Type = QueueClass
_HwBRASQoSPortQueueServiceId_Object = MibTableColumn
hwBRASQoSPortQueueServiceId = _HwBRASQoSPortQueueServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 2),
    _HwBRASQoSPortQueueServiceId_Type()
)
hwBRASQoSPortQueueServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueServiceId.setStatus("current")
_HwBRASQoSPortQueueScheduleStyle_Type = SchedulerService
_HwBRASQoSPortQueueScheduleStyle_Object = MibTableColumn
hwBRASQoSPortQueueScheduleStyle = _HwBRASQoSPortQueueScheduleStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 3),
    _HwBRASQoSPortQueueScheduleStyle_Type()
)
hwBRASQoSPortQueueScheduleStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueScheduleStyle.setStatus("current")


class _HwBRASQoSPortQueueWfqWeight_Type(Integer32):
    """Custom type hwBRASQoSPortQueueWfqWeight based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100),
    )


_HwBRASQoSPortQueueWfqWeight_Type.__name__ = "Integer32"
_HwBRASQoSPortQueueWfqWeight_Object = MibTableColumn
hwBRASQoSPortQueueWfqWeight = _HwBRASQoSPortQueueWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 4),
    _HwBRASQoSPortQueueWfqWeight_Type()
)
hwBRASQoSPortQueueWfqWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueWfqWeight.setStatus("current")


class _HwBRASQoSPortQueueShapingValue_Type(Integer32):
    """Custom type hwBRASQoSPortQueueShapingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwBRASQoSPortQueueShapingValue_Type.__name__ = "Integer32"
_HwBRASQoSPortQueueShapingValue_Object = MibTableColumn
hwBRASQoSPortQueueShapingValue = _HwBRASQoSPortQueueShapingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 5),
    _HwBRASQoSPortQueueShapingValue_Type()
)
hwBRASQoSPortQueueShapingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueShapingValue.setStatus("current")


class _HwBRASQoSPortQueueShaingPercentage_Type(Integer32):
    """Custom type hwBRASQoSPortQueueShaingPercentage based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSPortQueueShaingPercentage_Type.__name__ = "Integer32"
_HwBRASQoSPortQueueShaingPercentage_Object = MibTableColumn
hwBRASQoSPortQueueShaingPercentage = _HwBRASQoSPortQueueShaingPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 6),
    _HwBRASQoSPortQueueShaingPercentage_Type()
)
hwBRASQoSPortQueueShaingPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueShaingPercentage.setStatus("current")


class _HwBRASQoSPortQueuePortWredName_Type(OctetString):
    """Custom type hwBRASQoSPortQueuePortWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSPortQueuePortWredName_Type.__name__ = "OctetString"
_HwBRASQoSPortQueuePortWredName_Object = MibTableColumn
hwBRASQoSPortQueuePortWredName = _HwBRASQoSPortQueuePortWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 7),
    _HwBRASQoSPortQueuePortWredName_Type()
)
hwBRASQoSPortQueuePortWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueuePortWredName.setStatus("current")
_HwBRASQoSPortQueueRowStatus_Type = RowStatus
_HwBRASQoSPortQueueRowStatus_Object = MibTableColumn
hwBRASQoSPortQueueRowStatus = _HwBRASQoSPortQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 13, 1, 8),
    _HwBRASQoSPortQueueRowStatus_Type()
)
hwBRASQoSPortQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortQueueRowStatus.setStatus("current")
_HwBRASQoSPortWredTable_Object = MibTable
hwBRASQoSPortWredTable = _HwBRASQoSPortWredTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14)
)
if mibBuilder.loadTexts:
    hwBRASQoSPortWredTable.setStatus("current")
_HwBRASQoSPortWredEntry_Object = MibTableRow
hwBRASQoSPortWredEntry = _HwBRASQoSPortWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1)
)
hwBRASQoSPortWredEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredName"),
)
if mibBuilder.loadTexts:
    hwBRASQoSPortWredEntry.setStatus("current")


class _HwBRASQoSPortWredName_Type(OctetString):
    """Custom type hwBRASQoSPortWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSPortWredName_Type.__name__ = "OctetString"
_HwBRASQoSPortWredName_Object = MibTableColumn
hwBRASQoSPortWredName = _HwBRASQoSPortWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 1),
    _HwBRASQoSPortWredName_Type()
)
hwBRASQoSPortWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredName.setStatus("current")


class _HwBRASQoSPortWredGreenLowLimitValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredGreenLowLimitValue based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwBRASQoSPortWredGreenLowLimitValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredGreenLowLimitValue_Object = MibTableColumn
hwBRASQoSPortWredGreenLowLimitValue = _HwBRASQoSPortWredGreenLowLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 2),
    _HwBRASQoSPortWredGreenLowLimitValue_Type()
)
hwBRASQoSPortWredGreenLowLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredGreenLowLimitValue.setStatus("current")


class _HwBRASQoSPortWredGreenHighLimitValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredGreenHighLimitValue based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwBRASQoSPortWredGreenHighLimitValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredGreenHighLimitValue_Object = MibTableColumn
hwBRASQoSPortWredGreenHighLimitValue = _HwBRASQoSPortWredGreenHighLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 3),
    _HwBRASQoSPortWredGreenHighLimitValue_Type()
)
hwBRASQoSPortWredGreenHighLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredGreenHighLimitValue.setStatus("current")


class _HwBRASQoSPortWredGreenDiscardValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredGreenDiscardValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSPortWredGreenDiscardValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredGreenDiscardValue_Object = MibTableColumn
hwBRASQoSPortWredGreenDiscardValue = _HwBRASQoSPortWredGreenDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 4),
    _HwBRASQoSPortWredGreenDiscardValue_Type()
)
hwBRASQoSPortWredGreenDiscardValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredGreenDiscardValue.setStatus("current")


class _HwBRASQoSPortWredYellowLowLimitValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredYellowLowLimitValue based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwBRASQoSPortWredYellowLowLimitValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredYellowLowLimitValue_Object = MibTableColumn
hwBRASQoSPortWredYellowLowLimitValue = _HwBRASQoSPortWredYellowLowLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 5),
    _HwBRASQoSPortWredYellowLowLimitValue_Type()
)
hwBRASQoSPortWredYellowLowLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredYellowLowLimitValue.setStatus("current")


class _HwBRASQoSPortWredYellowHighLimitValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredYellowHighLimitValue based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwBRASQoSPortWredYellowHighLimitValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredYellowHighLimitValue_Object = MibTableColumn
hwBRASQoSPortWredYellowHighLimitValue = _HwBRASQoSPortWredYellowHighLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 6),
    _HwBRASQoSPortWredYellowHighLimitValue_Type()
)
hwBRASQoSPortWredYellowHighLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredYellowHighLimitValue.setStatus("current")


class _HwBRASQoSPortWredYellowDiscardValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredYellowDiscardValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSPortWredYellowDiscardValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredYellowDiscardValue_Object = MibTableColumn
hwBRASQoSPortWredYellowDiscardValue = _HwBRASQoSPortWredYellowDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 7),
    _HwBRASQoSPortWredYellowDiscardValue_Type()
)
hwBRASQoSPortWredYellowDiscardValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredYellowDiscardValue.setStatus("current")


class _HwBRASQoSPortWredRedLowLimitValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredRedLowLimitValue based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwBRASQoSPortWredRedLowLimitValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredRedLowLimitValue_Object = MibTableColumn
hwBRASQoSPortWredRedLowLimitValue = _HwBRASQoSPortWredRedLowLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 8),
    _HwBRASQoSPortWredRedLowLimitValue_Type()
)
hwBRASQoSPortWredRedLowLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredRedLowLimitValue.setStatus("current")


class _HwBRASQoSPortWredRedHighLimitValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredRedHighLimitValue based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwBRASQoSPortWredRedHighLimitValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredRedHighLimitValue_Object = MibTableColumn
hwBRASQoSPortWredRedHighLimitValue = _HwBRASQoSPortWredRedHighLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 9),
    _HwBRASQoSPortWredRedHighLimitValue_Type()
)
hwBRASQoSPortWredRedHighLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredRedHighLimitValue.setStatus("current")


class _HwBRASQoSPortWredRedDiscardValue_Type(Integer32):
    """Custom type hwBRASQoSPortWredRedDiscardValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBRASQoSPortWredRedDiscardValue_Type.__name__ = "Integer32"
_HwBRASQoSPortWredRedDiscardValue_Object = MibTableColumn
hwBRASQoSPortWredRedDiscardValue = _HwBRASQoSPortWredRedDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 10),
    _HwBRASQoSPortWredRedDiscardValue_Type()
)
hwBRASQoSPortWredRedDiscardValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredRedDiscardValue.setStatus("current")
_HwBRASQoSPortWredRowStatus_Type = RowStatus
_HwBRASQoSPortWredRowStatus_Object = MibTableColumn
hwBRASQoSPortWredRowStatus = _HwBRASQoSPortWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 14, 1, 11),
    _HwBRASQoSPortWredRowStatus_Type()
)
hwBRASQoSPortWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSPortWredRowStatus.setStatus("current")
_HwBRASQoSCarProfileTable_Object = MibTable
hwBRASQoSCarProfileTable = _HwBRASQoSCarProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15)
)
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileTable.setStatus("current")
_HwBRASQoSCarProfileEntry_Object = MibTableRow
hwBRASQoSCarProfileEntry = _HwBRASQoSCarProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1)
)
hwBRASQoSCarProfileEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfileIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileEntry.setStatus("current")


class _HwBRASQoSCarProfileIndex_Type(Integer32):
    """Custom type hwBRASQoSCarProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBRASQoSCarProfileIndex_Type.__name__ = "Integer32"
_HwBRASQoSCarProfileIndex_Object = MibTableColumn
hwBRASQoSCarProfileIndex = _HwBRASQoSCarProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 1),
    _HwBRASQoSCarProfileIndex_Type()
)
hwBRASQoSCarProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileIndex.setStatus("current")


class _HwBRASQoSCarProfileName_Type(OctetString):
    """Custom type hwBRASQoSCarProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSCarProfileName_Type.__name__ = "OctetString"
_HwBRASQoSCarProfileName_Object = MibTableColumn
hwBRASQoSCarProfileName = _HwBRASQoSCarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 2),
    _HwBRASQoSCarProfileName_Type()
)
hwBRASQoSCarProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileName.setStatus("current")


class _HwBRASQoSCarProfileCir_Type(Integer32):
    """Custom type hwBRASQoSCarProfileCir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(100, 10000000),
    )


_HwBRASQoSCarProfileCir_Type.__name__ = "Integer32"
_HwBRASQoSCarProfileCir_Object = MibTableColumn
hwBRASQoSCarProfileCir = _HwBRASQoSCarProfileCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 3),
    _HwBRASQoSCarProfileCir_Type()
)
hwBRASQoSCarProfileCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileCir.setStatus("current")


class _HwBRASQoSCarProfilePir_Type(Integer32):
    """Custom type hwBRASQoSCarProfilePir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(100, 10000000),
    )


_HwBRASQoSCarProfilePir_Type.__name__ = "Integer32"
_HwBRASQoSCarProfilePir_Object = MibTableColumn
hwBRASQoSCarProfilePir = _HwBRASQoSCarProfilePir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 4),
    _HwBRASQoSCarProfilePir_Type()
)
hwBRASQoSCarProfilePir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfilePir.setStatus("current")


class _HwBRASQoSCarProfileCbs_Type(Integer32):
    """Custom type hwBRASQoSCarProfileCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 33554432),
    )


_HwBRASQoSCarProfileCbs_Type.__name__ = "Integer32"
_HwBRASQoSCarProfileCbs_Object = MibTableColumn
hwBRASQoSCarProfileCbs = _HwBRASQoSCarProfileCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 5),
    _HwBRASQoSCarProfileCbs_Type()
)
hwBRASQoSCarProfileCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileCbs.setStatus("current")


class _HwBRASQoSCarProfilePbs_Type(Integer32):
    """Custom type hwBRASQoSCarProfilePbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33554432),
    )


_HwBRASQoSCarProfilePbs_Type.__name__ = "Integer32"
_HwBRASQoSCarProfilePbs_Object = MibTableColumn
hwBRASQoSCarProfilePbs = _HwBRASQoSCarProfilePbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 6),
    _HwBRASQoSCarProfilePbs_Type()
)
hwBRASQoSCarProfilePbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfilePbs.setStatus("current")
_HwBRASQoSCarProfileRowStatus_Type = RowStatus
_HwBRASQoSCarProfileRowStatus_Object = MibTableColumn
hwBRASQoSCarProfileRowStatus = _HwBRASQoSCarProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 15, 1, 7),
    _HwBRASQoSCarProfileRowStatus_Type()
)
hwBRASQoSCarProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSCarProfileRowStatus.setStatus("current")
_HwBRASQoSSlotTable_Object = MibTable
hwBRASQoSSlotTable = _HwBRASQoSSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16)
)
if mibBuilder.loadTexts:
    hwBRASQoSSlotTable.setStatus("current")
_HwBRASQoSSlotEntry_Object = MibTableRow
hwBRASQoSSlotEntry = _HwBRASQoSSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1)
)
hwBRASQoSSlotEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotId"),
)
if mibBuilder.loadTexts:
    hwBRASQoSSlotEntry.setStatus("current")


class _HwBRASQoSSlotId_Type(Integer32):
    """Custom type hwBRASQoSSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBRASQoSSlotId_Type.__name__ = "Integer32"
_HwBRASQoSSlotId_Object = MibTableColumn
hwBRASQoSSlotId = _HwBRASQoSSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 1),
    _HwBRASQoSSlotId_Type()
)
hwBRASQoSSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotId.setStatus("current")


class _HwBRASQoSSlotLinkLayerExclude_Type(TruthValue):
    """Custom type hwBRASQoSSlotLinkLayerExclude based on TruthValue"""


_HwBRASQoSSlotLinkLayerExclude_Object = MibTableColumn
hwBRASQoSSlotLinkLayerExclude = _HwBRASQoSSlotLinkLayerExclude_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 2),
    _HwBRASQoSSlotLinkLayerExclude_Type()
)
hwBRASQoSSlotLinkLayerExclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSSlotLinkLayerExclude.setStatus("current")


class _HwBRASQoSSlotEtherAjustOverhead_Type(Integer32):
    """Custom type hwBRASQoSSlotEtherAjustOverhead based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-35, 50),
    )


_HwBRASQoSSlotEtherAjustOverhead_Type.__name__ = "Integer32"
_HwBRASQoSSlotEtherAjustOverhead_Object = MibTableColumn
hwBRASQoSSlotEtherAjustOverhead = _HwBRASQoSSlotEtherAjustOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 3),
    _HwBRASQoSSlotEtherAjustOverhead_Type()
)
hwBRASQoSSlotEtherAjustOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSSlotEtherAjustOverhead.setStatus("current")


class _HwBRASQoSSlotRemoteAdjustEnableStatus_Type(TruthValue):
    """Custom type hwBRASQoSSlotRemoteAdjustEnableStatus based on TruthValue"""


_HwBRASQoSSlotRemoteAdjustEnableStatus_Object = MibTableColumn
hwBRASQoSSlotRemoteAdjustEnableStatus = _HwBRASQoSSlotRemoteAdjustEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 4),
    _HwBRASQoSSlotRemoteAdjustEnableStatus_Type()
)
hwBRASQoSSlotRemoteAdjustEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSSlotRemoteAdjustEnableStatus.setStatus("current")
_HwBRASQoSSlotInboundGqUsedNum_Type = Integer32
_HwBRASQoSSlotInboundGqUsedNum_Object = MibTableColumn
hwBRASQoSSlotInboundGqUsedNum = _HwBRASQoSSlotInboundGqUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 5),
    _HwBRASQoSSlotInboundGqUsedNum_Type()
)
hwBRASQoSSlotInboundGqUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotInboundGqUsedNum.setStatus("current")
_HwBRASQoSSlotInboundSqUsedNum_Type = Integer32
_HwBRASQoSSlotInboundSqUsedNum_Object = MibTableColumn
hwBRASQoSSlotInboundSqUsedNum = _HwBRASQoSSlotInboundSqUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 6),
    _HwBRASQoSSlotInboundSqUsedNum_Type()
)
hwBRASQoSSlotInboundSqUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotInboundSqUsedNum.setStatus("current")
_HwBRASQoSSlotInboundGqFreeNum_Type = Integer32
_HwBRASQoSSlotInboundGqFreeNum_Object = MibTableColumn
hwBRASQoSSlotInboundGqFreeNum = _HwBRASQoSSlotInboundGqFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 7),
    _HwBRASQoSSlotInboundGqFreeNum_Type()
)
hwBRASQoSSlotInboundGqFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotInboundGqFreeNum.setStatus("current")
_HwBRASQoSSlotInboundSqFreeNum_Type = Integer32
_HwBRASQoSSlotInboundSqFreeNum_Object = MibTableColumn
hwBRASQoSSlotInboundSqFreeNum = _HwBRASQoSSlotInboundSqFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 8),
    _HwBRASQoSSlotInboundSqFreeNum_Type()
)
hwBRASQoSSlotInboundSqFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotInboundSqFreeNum.setStatus("current")
_HwBRASQoSSlotOutboundGqUsedNum_Type = Integer32
_HwBRASQoSSlotOutboundGqUsedNum_Object = MibTableColumn
hwBRASQoSSlotOutboundGqUsedNum = _HwBRASQoSSlotOutboundGqUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 9),
    _HwBRASQoSSlotOutboundGqUsedNum_Type()
)
hwBRASQoSSlotOutboundGqUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotOutboundGqUsedNum.setStatus("current")
_HwBRASQoSSlotOutboundSqUsedNum_Type = Integer32
_HwBRASQoSSlotOutboundSqUsedNum_Object = MibTableColumn
hwBRASQoSSlotOutboundSqUsedNum = _HwBRASQoSSlotOutboundSqUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 10),
    _HwBRASQoSSlotOutboundSqUsedNum_Type()
)
hwBRASQoSSlotOutboundSqUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotOutboundSqUsedNum.setStatus("current")
_HwBRASQoSSlotOutboundGqFreeNum_Type = Integer32
_HwBRASQoSSlotOutboundGqFreeNum_Object = MibTableColumn
hwBRASQoSSlotOutboundGqFreeNum = _HwBRASQoSSlotOutboundGqFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 11),
    _HwBRASQoSSlotOutboundGqFreeNum_Type()
)
hwBRASQoSSlotOutboundGqFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotOutboundGqFreeNum.setStatus("current")
_HwBRASQoSSlotOutboundSqFreeNum_Type = Integer32
_HwBRASQoSSlotOutboundSqFreeNum_Object = MibTableColumn
hwBRASQoSSlotOutboundSqFreeNum = _HwBRASQoSSlotOutboundSqFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 12),
    _HwBRASQoSSlotOutboundSqFreeNum_Type()
)
hwBRASQoSSlotOutboundSqFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotOutboundSqFreeNum.setStatus("current")
_HwBRASQoSSlotActiveStatus_Type = TruthValue
_HwBRASQoSSlotActiveStatus_Object = MibTableColumn
hwBRASQoSSlotActiveStatus = _HwBRASQoSSlotActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 16, 1, 13),
    _HwBRASQoSSlotActiveStatus_Type()
)
hwBRASQoSSlotActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSSlotActiveStatus.setStatus("current")
_HwBRASQoSMultiShapingTable_Object = MibTable
hwBRASQoSMultiShapingTable = _HwBRASQoSMultiShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17)
)
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingTable.setStatus("current")
_HwBRASQoSMultiShapingEntry_Object = MibTableRow
hwBRASQoSMultiShapingEntry = _HwBRASQoSMultiShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1)
)
hwBRASQoSMultiShapingEntry.setIndexNames(
    (0, "HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingIndex"),
)
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingEntry.setStatus("current")


class _HwBRASQoSMultiShapingIndex_Type(Integer32):
    """Custom type hwBRASQoSMultiShapingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwBRASQoSMultiShapingIndex_Type.__name__ = "Integer32"
_HwBRASQoSMultiShapingIndex_Object = MibTableColumn
hwBRASQoSMultiShapingIndex = _HwBRASQoSMultiShapingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 1),
    _HwBRASQoSMultiShapingIndex_Type()
)
hwBRASQoSMultiShapingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingIndex.setStatus("current")


class _HwBRASQoSMultiShapingName_Type(OctetString):
    """Custom type hwBRASQoSMultiShapingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASQoSMultiShapingName_Type.__name__ = "OctetString"
_HwBRASQoSMultiShapingName_Object = MibTableColumn
hwBRASQoSMultiShapingName = _HwBRASQoSMultiShapingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 2),
    _HwBRASQoSMultiShapingName_Type()
)
hwBRASQoSMultiShapingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingName.setStatus("current")


class _HwBRASQoSMultiShapingEndIndex_Type(Integer32):
    """Custom type hwBRASQoSMultiShapingEndIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwBRASQoSMultiShapingEndIndex_Type.__name__ = "Integer32"
_HwBRASQoSMultiShapingEndIndex_Object = MibTableColumn
hwBRASQoSMultiShapingEndIndex = _HwBRASQoSMultiShapingEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 3),
    _HwBRASQoSMultiShapingEndIndex_Type()
)
hwBRASQoSMultiShapingEndIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingEndIndex.setStatus("current")


class _HwBRASQoSMultiShapingCir_Type(Integer32):
    """Custom type hwBRASQoSMultiShapingCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 1000000),
    )


_HwBRASQoSMultiShapingCir_Type.__name__ = "Integer32"
_HwBRASQoSMultiShapingCir_Object = MibTableColumn
hwBRASQoSMultiShapingCir = _HwBRASQoSMultiShapingCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 4),
    _HwBRASQoSMultiShapingCir_Type()
)
hwBRASQoSMultiShapingCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingCir.setStatus("current")


class _HwBRASQoSMultiShapingPir_Type(Integer32):
    """Custom type hwBRASQoSMultiShapingPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(70, 10000000),
    )


_HwBRASQoSMultiShapingPir_Type.__name__ = "Integer32"
_HwBRASQoSMultiShapingPir_Object = MibTableColumn
hwBRASQoSMultiShapingPir = _HwBRASQoSMultiShapingPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 5),
    _HwBRASQoSMultiShapingPir_Type()
)
hwBRASQoSMultiShapingPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingPir.setStatus("current")


class _HwBRASQoSMultiShapingQueueLength_Type(Integer32):
    """Custom type hwBRASQoSMultiShapingQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 128000),
    )


_HwBRASQoSMultiShapingQueueLength_Type.__name__ = "Integer32"
_HwBRASQoSMultiShapingQueueLength_Object = MibTableColumn
hwBRASQoSMultiShapingQueueLength = _HwBRASQoSMultiShapingQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 6),
    _HwBRASQoSMultiShapingQueueLength_Type()
)
hwBRASQoSMultiShapingQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingQueueLength.setStatus("current")
_HwBRASQoSMultiShapingRowStatus_Type = RowStatus
_HwBRASQoSMultiShapingRowStatus_Object = MibTableColumn
hwBRASQoSMultiShapingRowStatus = _HwBRASQoSMultiShapingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 1, 17, 1, 7),
    _HwBRASQoSMultiShapingRowStatus_Type()
)
hwBRASQoSMultiShapingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBRASQoSMultiShapingRowStatus.setStatus("current")
_HwBRASQoSMibTrap_ObjectIdentity = ObjectIdentity
hwBRASQoSMibTrap = _HwBRASQoSMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2)
)
_HwBRASQoSTrapOid_ObjectIdentity = ObjectIdentity
hwBRASQoSTrapOid = _HwBRASQoSTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1)
)


class _HwBRASQoSTrapSlotID_Type(Integer32):
    """Custom type hwBRASQoSTrapSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBRASQoSTrapSlotID_Type.__name__ = "Integer32"
_HwBRASQoSTrapSlotID_Object = MibScalar
hwBRASQoSTrapSlotID = _HwBRASQoSTrapSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 1),
    _HwBRASQoSTrapSlotID_Type()
)
hwBRASQoSTrapSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapSlotID.setStatus("current")
_HwBRASQoSFailBandwidth_Type = Integer32
_HwBRASQoSFailBandwidth_Object = MibScalar
hwBRASQoSFailBandwidth = _HwBRASQoSFailBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 2),
    _HwBRASQoSFailBandwidth_Type()
)
hwBRASQoSFailBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSFailBandwidth.setStatus("current")


class _HwBRASQoSTrapUserBehavior_Type(Integer32):
    """Custom type hwBRASQoSTrapUserBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alloc", 1),
          ("free", 3),
          ("update", 2))
    )


_HwBRASQoSTrapUserBehavior_Type.__name__ = "Integer32"
_HwBRASQoSTrapUserBehavior_Object = MibScalar
hwBRASQoSTrapUserBehavior = _HwBRASQoSTrapUserBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 3),
    _HwBRASQoSTrapUserBehavior_Type()
)
hwBRASQoSTrapUserBehavior.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapUserBehavior.setStatus("current")
_HwBRASQoSTrapUserID_Type = Integer32
_HwBRASQoSTrapUserID_Object = MibScalar
hwBRASQoSTrapUserID = _HwBRASQoSTrapUserID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 4),
    _HwBRASQoSTrapUserID_Type()
)
hwBRASQoSTrapUserID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapUserID.setStatus("current")


class _HwBRASQoSTrapTunnelID_Type(Integer32):
    """Custom type hwBRASQoSTrapTunnelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_HwBRASQoSTrapTunnelID_Type.__name__ = "Integer32"
_HwBRASQoSTrapTunnelID_Object = MibScalar
hwBRASQoSTrapTunnelID = _HwBRASQoSTrapTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 5),
    _HwBRASQoSTrapTunnelID_Type()
)
hwBRASQoSTrapTunnelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapTunnelID.setStatus("current")


class _HwBRASQoSTrapQinqVlan_Type(VlanIndex):
    """Custom type hwBRASQoSTrapQinqVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwBRASQoSTrapQinqVlan_Type.__name__ = "VlanIndex"
_HwBRASQoSTrapQinqVlan_Object = MibScalar
hwBRASQoSTrapQinqVlan = _HwBRASQoSTrapQinqVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 6),
    _HwBRASQoSTrapQinqVlan_Type()
)
hwBRASQoSTrapQinqVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapQinqVlan.setStatus("current")


class _HwBRASQoSTrapVlan_Type(VlanIndex):
    """Custom type hwBRASQoSTrapVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwBRASQoSTrapVlan_Type.__name__ = "VlanIndex"
_HwBRASQoSTrapVlan_Object = MibScalar
hwBRASQoSTrapVlan = _HwBRASQoSTrapVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 7),
    _HwBRASQoSTrapVlan_Type()
)
hwBRASQoSTrapVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapVlan.setStatus("current")
_HwBRASQoSTrapIfindex_Type = InterfaceIndex
_HwBRASQoSTrapIfindex_Object = MibScalar
hwBRASQoSTrapIfindex = _HwBRASQoSTrapIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 1, 8),
    _HwBRASQoSTrapIfindex_Type()
)
hwBRASQoSTrapIfindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBRASQoSTrapIfindex.setStatus("current")
_HwBRASQoSTrapDefine_ObjectIdentity = ObjectIdentity
hwBRASQoSTrapDefine = _HwBRASQoSTrapDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2)
)
_HwBRASQoSTraps_ObjectIdentity = ObjectIdentity
hwBRASQoSTraps = _HwBRASQoSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1)
)
_HwBrasQosConformance_ObjectIdentity = ObjectIdentity
hwBrasQosConformance = _HwBrasQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3)
)
_HwBrasQosCompliances_ObjectIdentity = ObjectIdentity
hwBrasQosCompliances = _HwBrasQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 1)
)
_HwBrasQosGroups_ObjectIdentity = ObjectIdentity
hwBrasQosGroups = _HwBrasQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2)
)

# Managed Objects groups

hwBrasQosQosProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 1)
)
hwBrasQosQosProfileGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileQueueName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileDropName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileSchedulerName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSFlowMappingName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSLinkAjustLength"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQoSProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosQosProfileGroup.setStatus("current")

hwBrasQosSchedulerProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 2)
)
hwBrasQosSchedulerProfileGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileGtsUpCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileGtsUpPir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileGtsUpLength"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileGtsDownCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileGtsDownPir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileGtsDownLength"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileUpCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileUpCbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileUpPir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileUpPbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileDownCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileDownCbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileDownPir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileDownPbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerProfileWfqWeight"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSchedulerRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosSchedulerProfileGroup.setStatus("current")

hwBrasQosDropProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 3)
)
hwBrasQosDropProfileGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailBeThreshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailAf1Threshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailAf2Threshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailAf3Threshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailAf4Threshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailEfThreshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailCs6Threshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileTailCs7Threshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredMaxThreshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredMinThreshold"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredGreenHighValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredGreenLowValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredGreenMaxDrop"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredYellowHighValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredYellowLowValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredYellowMaxDrop"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredRedHighValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredRedLowValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredRedMaxDrop"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredUserDefHighValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredUserDefLowValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileWredUserDefMaxDrop"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSDropProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosDropProfileGroup.setStatus("current")

hwBrasQosQueueProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 4)
)
hwBrasQosQueueProfileGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileBeStyle"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileAf1Style"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileAf2Style"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileAf3Style"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileAf4Style"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileEfStyle"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileCs6Style"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileCs7Style"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosQueueProfileGroup.setStatus("current")

hwBrasQosQueueClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 5)
)
hwBrasQosQueueClassGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassServiceId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassWredEnableStatus"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassWredWeight"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassWrrWeight"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassLength"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassCbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassPir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassPbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassWfqWeight"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassShaping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassScheduler"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSQueueClassDropName"))
)
if mibBuilder.loadTexts:
    hwBrasQosQueueClassGroup.setStatus("current")

hwBrasQosFlowMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 6)
)
hwBrasQosFlowMappingGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSFlowMappingName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSBeMapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSAf1Mapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSAf2Mapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSAf3Mapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSAf4Mapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSEfMapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCs6Mapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCs7Mapping"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSFlowMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosFlowMappingGroup.setStatus("current")

hwBrasQosIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 7)
)
hwBrasQosIfGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfQoSProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfScheduleId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfServiceGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfShapingValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVpGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfInboundVcGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfOutboundAVcGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfOutboundBVcGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfInboundGVpGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfOutboundAGVpGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfPacketAjustOverhead"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfRemoteLinkMode"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfInCarProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfInStatistics"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfOutCarProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfOutStatistics"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVplsCarStatus"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfMultiShapingStatus"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfActiveStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosIfGroup.setStatus("current")

hwBrasQosIfVcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 8)
)
hwBrasQosIfVcGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcIfIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcVlanId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcQinqVlanId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcVlanEndId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcQinqVlanEndId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcVcGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcServiceGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcInCarProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcInStatistics"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcInCarEachVlanStatus"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcOutCarProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcOutStatistics"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVcOutCarEachVlanStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosIfVcGroup.setStatus("current")

hwBrasQosVpGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 9)
)
hwBrasQosVpGroupGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupIfIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupQosProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVpGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosVpGroupGroup.setStatus("current")

hwBrasQosVcGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 10)
)
hwBrasQosVcGroupGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVcGroupIfIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVcGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVcGroupQosProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSVcGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosVcGroupGroup.setStatus("current")

hwBrasQosGVpGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 11)
)
hwBrasQosGVpGroupGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSGVpGroupSlotId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSGVpGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSGVpGroupQosProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSGVpGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosGVpGroupGroup.setStatus("current")

hwBrasQosServiceGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 12)
)
hwBrasQosServiceGroupGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSServiceGroupIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSServiceGroupName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSServiceGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosServiceGroupGroup.setStatus("current")

hwBrasQosPortQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 13)
)
hwBrasQosPortQueueGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueIfIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueServiceId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueScheduleStyle"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueWfqWeight"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueShapingValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueShaingPercentage"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueuePortWredName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosPortQueueGroup.setStatus("current")

hwBrasQosPortWredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 14)
)
hwBrasQosPortWredGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredGreenLowLimitValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredGreenHighLimitValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredGreenDiscardValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredYellowLowLimitValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredYellowHighLimitValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredYellowDiscardValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredRedLowLimitValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredRedHighLimitValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredRedDiscardValue"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSPortWredRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosPortWredGroup.setStatus("current")

hwBrasQosCarProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 15)
)
hwBrasQosCarProfileGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfileIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfileName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfileCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfilePir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfileCbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfilePbs"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSCarProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosCarProfileGroup.setStatus("current")

hwBrasQosSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 16)
)
hwBrasQosSlotGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotId"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotLinkLayerExclude"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotEtherAjustOverhead"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotRemoteAdjustEnableStatus"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotInboundGqUsedNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotInboundSqUsedNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotInboundGqFreeNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotInboundSqFreeNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotOutboundGqUsedNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotOutboundSqUsedNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotOutboundGqFreeNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotOutboundSqFreeNum"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSSlotActiveStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosSlotGroup.setStatus("current")

hwBrasQosMultiShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 17)
)
hwBrasQosMultiShapingGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingName"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingEndIndex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingCir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingPir"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingQueueLength"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSMultiShapingRowStatus"))
)
if mibBuilder.loadTexts:
    hwBrasQosMultiShapingGroup.setStatus("current")

hwBrasQosTrapOidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 18)
)
hwBrasQosTrapOidGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapSlotID"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSFailBandwidth"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapUserBehavior"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapUserID"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapTunnelID"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapQinqVlan"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapVlan"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapIfindex"))
)
if mibBuilder.loadTexts:
    hwBrasQosTrapOidGroup.setStatus("current")


# Notification objects

hwBRASQoSIfResFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 1)
)
hwBRASQoSIfResFail.setObjects(
    ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapIfindex")
)
if mibBuilder.loadTexts:
    hwBRASQoSIfResFail.setStatus(
        "current"
    )

hwBRASQoSIfVlanResFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 2)
)
hwBRASQoSIfVlanResFail.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapIfindex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapVlan"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapQinqVlan"))
)
if mibBuilder.loadTexts:
    hwBRASQoSIfVlanResFail.setStatus(
        "current"
    )

hwBRASQoSTunnelResFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 3)
)
hwBRASQoSTunnelResFail.setObjects(
    ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapTunnelID")
)
if mibBuilder.loadTexts:
    hwBRASQoSTunnelResFail.setStatus(
        "current"
    )

hwBRASQoSUserResFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 4)
)
hwBRASQoSUserResFail.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapUserID"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapUserBehavior"))
)
if mibBuilder.loadTexts:
    hwBRASQoSUserResFail.setStatus(
        "current"
    )

hwBRASQoSTrunkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 5)
)
hwBRASQoSTrunkFail.setObjects(
    ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapIfindex")
)
if mibBuilder.loadTexts:
    hwBRASQoSTrunkFail.setStatus(
        "current"
    )

hwBRASQoSUserBandwidthOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 6)
)
hwBRASQoSUserBandwidthOverflow.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapIfindex"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapUserID"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSFailBandwidth"))
)
if mibBuilder.loadTexts:
    hwBRASQoSUserBandwidthOverflow.setStatus(
        "current"
    )

hwBRASQoSTMExcepion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 2, 2, 1, 7)
)
hwBRASQoSTMExcepion.setObjects(
    ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrapSlotID")
)
if mibBuilder.loadTexts:
    hwBRASQoSTMExcepion.setStatus(
        "current"
    )


# Notifications groups

hwBrasQosTrapDefineGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 2, 19)
)
hwBrasQosTrapDefineGroup.setObjects(
      *(("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfResFail"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSIfVlanResFail"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTunnelResFail"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSUserResFail"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTrunkFail"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSUserBandwidthOverflow"),
        ("HUAWEI-BRAS-QOS-MIB", "hwBRASQoSTMExcepion"))
)
if mibBuilder.loadTexts:
    hwBrasQosTrapDefineGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwBrasQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwBrasQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-QOS-MIB",
    **{"SchedulerStyle": SchedulerStyle,
       "QueueClass": QueueClass,
       "SchedulerService": SchedulerService,
       "InterfaceScheduler": InterfaceScheduler,
       "LinkMode": LinkMode,
       "StatMode": StatMode,
       "hwBRASQoS": hwBRASQoS,
       "hwBRASQoSObjects": hwBRASQoSObjects,
       "hwBRASQoSQoSProfileTable": hwBRASQoSQoSProfileTable,
       "hwBRASQoSQoSProfileEntry": hwBRASQoSQoSProfileEntry,
       "hwBRASQoSQoSProfileIndex": hwBRASQoSQoSProfileIndex,
       "hwBRASQoSQoSProfileName": hwBRASQoSQoSProfileName,
       "hwBRASQoSQoSProfileQueueName": hwBRASQoSQoSProfileQueueName,
       "hwBRASQoSQoSProfileDropName": hwBRASQoSQoSProfileDropName,
       "hwBRASQoSQoSProfileSchedulerName": hwBRASQoSQoSProfileSchedulerName,
       "hwBRASQoSQoSFlowMappingName": hwBRASQoSQoSFlowMappingName,
       "hwBRASQoSQoSLinkAjustLength": hwBRASQoSQoSLinkAjustLength,
       "hwBRASQoSQoSProfileRowStatus": hwBRASQoSQoSProfileRowStatus,
       "hwBRASQoSSchedulerProfileTable": hwBRASQoSSchedulerProfileTable,
       "hwBRASQoSSchedulerProfileEntry": hwBRASQoSSchedulerProfileEntry,
       "hwBRASQoSSchedulerProfileIndex": hwBRASQoSSchedulerProfileIndex,
       "hwBRASQoSSchedulerProfileName": hwBRASQoSSchedulerProfileName,
       "hwBRASQoSSchedulerProfileGtsUpCir": hwBRASQoSSchedulerProfileGtsUpCir,
       "hwBRASQoSSchedulerProfileGtsUpPir": hwBRASQoSSchedulerProfileGtsUpPir,
       "hwBRASQoSSchedulerProfileGtsUpLength": hwBRASQoSSchedulerProfileGtsUpLength,
       "hwBRASQoSSchedulerProfileGtsDownCir": hwBRASQoSSchedulerProfileGtsDownCir,
       "hwBRASQoSSchedulerProfileGtsDownPir": hwBRASQoSSchedulerProfileGtsDownPir,
       "hwBRASQoSSchedulerProfileGtsDownLength": hwBRASQoSSchedulerProfileGtsDownLength,
       "hwBRASQoSSchedulerProfileUpCir": hwBRASQoSSchedulerProfileUpCir,
       "hwBRASQoSSchedulerProfileUpCbs": hwBRASQoSSchedulerProfileUpCbs,
       "hwBRASQoSSchedulerProfileUpPir": hwBRASQoSSchedulerProfileUpPir,
       "hwBRASQoSSchedulerProfileUpPbs": hwBRASQoSSchedulerProfileUpPbs,
       "hwBRASQoSSchedulerProfileDownCir": hwBRASQoSSchedulerProfileDownCir,
       "hwBRASQoSSchedulerProfileDownCbs": hwBRASQoSSchedulerProfileDownCbs,
       "hwBRASQoSSchedulerProfileDownPir": hwBRASQoSSchedulerProfileDownPir,
       "hwBRASQoSSchedulerProfileDownPbs": hwBRASQoSSchedulerProfileDownPbs,
       "hwBRASQoSSchedulerProfileWfqWeight": hwBRASQoSSchedulerProfileWfqWeight,
       "hwBRASQoSSchedulerRowStatus": hwBRASQoSSchedulerRowStatus,
       "hwBRASQoSDropProfileTable": hwBRASQoSDropProfileTable,
       "hwBRASQoSDropProfileEntry": hwBRASQoSDropProfileEntry,
       "hwBRASQoSDropProfileIndex": hwBRASQoSDropProfileIndex,
       "hwBRASQoSDropProfileName": hwBRASQoSDropProfileName,
       "hwBRASQoSDropProfileTailBeThreshold": hwBRASQoSDropProfileTailBeThreshold,
       "hwBRASQoSDropProfileTailAf1Threshold": hwBRASQoSDropProfileTailAf1Threshold,
       "hwBRASQoSDropProfileTailAf2Threshold": hwBRASQoSDropProfileTailAf2Threshold,
       "hwBRASQoSDropProfileTailAf3Threshold": hwBRASQoSDropProfileTailAf3Threshold,
       "hwBRASQoSDropProfileTailAf4Threshold": hwBRASQoSDropProfileTailAf4Threshold,
       "hwBRASQoSDropProfileTailEfThreshold": hwBRASQoSDropProfileTailEfThreshold,
       "hwBRASQoSDropProfileTailCs6Threshold": hwBRASQoSDropProfileTailCs6Threshold,
       "hwBRASQoSDropProfileTailCs7Threshold": hwBRASQoSDropProfileTailCs7Threshold,
       "hwBRASQoSDropProfileWredMaxThreshold": hwBRASQoSDropProfileWredMaxThreshold,
       "hwBRASQoSDropProfileWredMinThreshold": hwBRASQoSDropProfileWredMinThreshold,
       "hwBRASQoSDropProfileWredGreenHighValue": hwBRASQoSDropProfileWredGreenHighValue,
       "hwBRASQoSDropProfileWredGreenLowValue": hwBRASQoSDropProfileWredGreenLowValue,
       "hwBRASQoSDropProfileWredGreenMaxDrop": hwBRASQoSDropProfileWredGreenMaxDrop,
       "hwBRASQoSDropProfileWredYellowHighValue": hwBRASQoSDropProfileWredYellowHighValue,
       "hwBRASQoSDropProfileWredYellowLowValue": hwBRASQoSDropProfileWredYellowLowValue,
       "hwBRASQoSDropProfileWredYellowMaxDrop": hwBRASQoSDropProfileWredYellowMaxDrop,
       "hwBRASQoSDropProfileWredRedHighValue": hwBRASQoSDropProfileWredRedHighValue,
       "hwBRASQoSDropProfileWredRedLowValue": hwBRASQoSDropProfileWredRedLowValue,
       "hwBRASQoSDropProfileWredRedMaxDrop": hwBRASQoSDropProfileWredRedMaxDrop,
       "hwBRASQoSDropProfileWredUserDefHighValue": hwBRASQoSDropProfileWredUserDefHighValue,
       "hwBRASQoSDropProfileWredUserDefLowValue": hwBRASQoSDropProfileWredUserDefLowValue,
       "hwBRASQoSDropProfileWredUserDefMaxDrop": hwBRASQoSDropProfileWredUserDefMaxDrop,
       "hwBRASQoSDropProfileRowStatus": hwBRASQoSDropProfileRowStatus,
       "hwBRASQoSQueueProfileTable": hwBRASQoSQueueProfileTable,
       "hwBRASQoSQueueProfileEntry": hwBRASQoSQueueProfileEntry,
       "hwBRASQoSQueueProfileIndex": hwBRASQoSQueueProfileIndex,
       "hwBRASQoSQueueProfileName": hwBRASQoSQueueProfileName,
       "hwBRASQoSQueueProfileBeStyle": hwBRASQoSQueueProfileBeStyle,
       "hwBRASQoSQueueProfileAf1Style": hwBRASQoSQueueProfileAf1Style,
       "hwBRASQoSQueueProfileAf2Style": hwBRASQoSQueueProfileAf2Style,
       "hwBRASQoSQueueProfileAf3Style": hwBRASQoSQueueProfileAf3Style,
       "hwBRASQoSQueueProfileAf4Style": hwBRASQoSQueueProfileAf4Style,
       "hwBRASQoSQueueProfileEfStyle": hwBRASQoSQueueProfileEfStyle,
       "hwBRASQoSQueueProfileCs6Style": hwBRASQoSQueueProfileCs6Style,
       "hwBRASQoSQueueProfileCs7Style": hwBRASQoSQueueProfileCs7Style,
       "hwBRASQoSQueueProfileRowStatus": hwBRASQoSQueueProfileRowStatus,
       "hwBRASQoSQueueClassTable": hwBRASQoSQueueClassTable,
       "hwBRASQoSQueueClassEntry": hwBRASQoSQueueClassEntry,
       "hwBRASQoSQueueClassProfileName": hwBRASQoSQueueClassProfileName,
       "hwBRASQoSQueueClassServiceId": hwBRASQoSQueueClassServiceId,
       "hwBRASQoSQueueClassWredEnableStatus": hwBRASQoSQueueClassWredEnableStatus,
       "hwBRASQoSQueueClassWredWeight": hwBRASQoSQueueClassWredWeight,
       "hwBRASQoSQueueClassWrrWeight": hwBRASQoSQueueClassWrrWeight,
       "hwBRASQoSQueueClassLength": hwBRASQoSQueueClassLength,
       "hwBRASQoSQueueClassCir": hwBRASQoSQueueClassCir,
       "hwBRASQoSQueueClassCbs": hwBRASQoSQueueClassCbs,
       "hwBRASQoSQueueClassPir": hwBRASQoSQueueClassPir,
       "hwBRASQoSQueueClassPbs": hwBRASQoSQueueClassPbs,
       "hwBRASQoSQueueClassWfqWeight": hwBRASQoSQueueClassWfqWeight,
       "hwBRASQoSQueueClassShaping": hwBRASQoSQueueClassShaping,
       "hwBRASQoSQueueClassScheduler": hwBRASQoSQueueClassScheduler,
       "hwBRASQoSQueueClassDropName": hwBRASQoSQueueClassDropName,
       "hwBRASQoSFlowMappingTable": hwBRASQoSFlowMappingTable,
       "hwBRASQoSFlowMappingEntry": hwBRASQoSFlowMappingEntry,
       "hwBRASQoSFlowMappingName": hwBRASQoSFlowMappingName,
       "hwBRASQoSBeMapping": hwBRASQoSBeMapping,
       "hwBRASQoSAf1Mapping": hwBRASQoSAf1Mapping,
       "hwBRASQoSAf2Mapping": hwBRASQoSAf2Mapping,
       "hwBRASQoSAf3Mapping": hwBRASQoSAf3Mapping,
       "hwBRASQoSAf4Mapping": hwBRASQoSAf4Mapping,
       "hwBRASQoSEfMapping": hwBRASQoSEfMapping,
       "hwBRASQoSCs6Mapping": hwBRASQoSCs6Mapping,
       "hwBRASQoSCs7Mapping": hwBRASQoSCs7Mapping,
       "hwBRASQoSFlowMappingRowStatus": hwBRASQoSFlowMappingRowStatus,
       "hwBRASQoSIfTable": hwBRASQoSIfTable,
       "hwBRASQoSIfEntry": hwBRASQoSIfEntry,
       "hwBRASQoSIfIndex": hwBRASQoSIfIndex,
       "hwBRASQoSIfName": hwBRASQoSIfName,
       "hwBRASQoSIfQoSProfileName": hwBRASQoSIfQoSProfileName,
       "hwBRASQoSIfScheduleId": hwBRASQoSIfScheduleId,
       "hwBRASQoSIfServiceGroupName": hwBRASQoSIfServiceGroupName,
       "hwBRASQoSIfShapingValue": hwBRASQoSIfShapingValue,
       "hwBRASQoSIfVpGroupName": hwBRASQoSIfVpGroupName,
       "hwBRASQoSIfInboundVcGroupName": hwBRASQoSIfInboundVcGroupName,
       "hwBRASQoSIfOutboundAVcGroupName": hwBRASQoSIfOutboundAVcGroupName,
       "hwBRASQoSIfOutboundBVcGroupName": hwBRASQoSIfOutboundBVcGroupName,
       "hwBRASQoSIfInboundGVpGroupName": hwBRASQoSIfInboundGVpGroupName,
       "hwBRASQoSIfOutboundAGVpGroupName": hwBRASQoSIfOutboundAGVpGroupName,
       "hwBRASQoSIfPacketAjustOverhead": hwBRASQoSIfPacketAjustOverhead,
       "hwBRASQoSIfRemoteLinkMode": hwBRASQoSIfRemoteLinkMode,
       "hwBRASQoSIfInCarProfileName": hwBRASQoSIfInCarProfileName,
       "hwBRASQoSIfInStatistics": hwBRASQoSIfInStatistics,
       "hwBRASQoSIfOutCarProfileName": hwBRASQoSIfOutCarProfileName,
       "hwBRASQoSIfOutStatistics": hwBRASQoSIfOutStatistics,
       "hwBRASQoSIfVplsCarStatus": hwBRASQoSIfVplsCarStatus,
       "hwBRASQoSIfMultiShapingStatus": hwBRASQoSIfMultiShapingStatus,
       "hwBRASQoSIfActiveStatus": hwBRASQoSIfActiveStatus,
       "hwBRASQoSIfVcTable": hwBRASQoSIfVcTable,
       "hwBRASQoSIfVcEntry": hwBRASQoSIfVcEntry,
       "hwBRASQoSIfVcIfIndex": hwBRASQoSIfVcIfIndex,
       "hwBRASQoSIfVcVlanId": hwBRASQoSIfVcVlanId,
       "hwBRASQoSIfVcQinqVlanId": hwBRASQoSIfVcQinqVlanId,
       "hwBRASQoSIfVcVlanEndId": hwBRASQoSIfVcVlanEndId,
       "hwBRASQoSIfVcQinqVlanEndId": hwBRASQoSIfVcQinqVlanEndId,
       "hwBRASQoSIfVcVcGroupName": hwBRASQoSIfVcVcGroupName,
       "hwBRASQoSIfVcServiceGroupName": hwBRASQoSIfVcServiceGroupName,
       "hwBRASQoSIfVcInCarProfileName": hwBRASQoSIfVcInCarProfileName,
       "hwBRASQoSIfVcInStatistics": hwBRASQoSIfVcInStatistics,
       "hwBRASQoSIfVcInCarEachVlanStatus": hwBRASQoSIfVcInCarEachVlanStatus,
       "hwBRASQoSIfVcOutCarProfileName": hwBRASQoSIfVcOutCarProfileName,
       "hwBRASQoSIfVcOutStatistics": hwBRASQoSIfVcOutStatistics,
       "hwBRASQoSIfVcOutCarEachVlanStatus": hwBRASQoSIfVcOutCarEachVlanStatus,
       "hwBRASQoSVpGroupTable": hwBRASQoSVpGroupTable,
       "hwBRASQoSVpGroupEntry": hwBRASQoSVpGroupEntry,
       "hwBRASQoSVpGroupIfIndex": hwBRASQoSVpGroupIfIndex,
       "hwBRASQoSVpGroupName": hwBRASQoSVpGroupName,
       "hwBRASQoSVpGroupQosProfileName": hwBRASQoSVpGroupQosProfileName,
       "hwBRASQoSVpGroupRowStatus": hwBRASQoSVpGroupRowStatus,
       "hwBRASQoSVcGroupTable": hwBRASQoSVcGroupTable,
       "hwBRASQoSVcGroupEntry": hwBRASQoSVcGroupEntry,
       "hwBRASQoSVcGroupIfIndex": hwBRASQoSVcGroupIfIndex,
       "hwBRASQoSVcGroupName": hwBRASQoSVcGroupName,
       "hwBRASQoSVcGroupQosProfileName": hwBRASQoSVcGroupQosProfileName,
       "hwBRASQoSVcGroupRowStatus": hwBRASQoSVcGroupRowStatus,
       "hwBRASQoSGVpGroupTable": hwBRASQoSGVpGroupTable,
       "hwBRASQoSGVpGroupEntry": hwBRASQoSGVpGroupEntry,
       "hwBRASQoSGVpGroupSlotId": hwBRASQoSGVpGroupSlotId,
       "hwBRASQoSGVpGroupName": hwBRASQoSGVpGroupName,
       "hwBRASQoSGVpGroupQosProfileName": hwBRASQoSGVpGroupQosProfileName,
       "hwBRASQoSGVpGroupRowStatus": hwBRASQoSGVpGroupRowStatus,
       "hwBRASQoSServiceGroupTable": hwBRASQoSServiceGroupTable,
       "hwBRASQoSServiceGroupEntry": hwBRASQoSServiceGroupEntry,
       "hwBRASQoSServiceGroupIndex": hwBRASQoSServiceGroupIndex,
       "hwBRASQoSServiceGroupName": hwBRASQoSServiceGroupName,
       "hwBRASQoSServiceGroupRowStatus": hwBRASQoSServiceGroupRowStatus,
       "hwBRASQoSPortQueueTable": hwBRASQoSPortQueueTable,
       "hwBRASQoSPortQueueEntry": hwBRASQoSPortQueueEntry,
       "hwBRASQoSPortQueueIfIndex": hwBRASQoSPortQueueIfIndex,
       "hwBRASQoSPortQueueServiceId": hwBRASQoSPortQueueServiceId,
       "hwBRASQoSPortQueueScheduleStyle": hwBRASQoSPortQueueScheduleStyle,
       "hwBRASQoSPortQueueWfqWeight": hwBRASQoSPortQueueWfqWeight,
       "hwBRASQoSPortQueueShapingValue": hwBRASQoSPortQueueShapingValue,
       "hwBRASQoSPortQueueShaingPercentage": hwBRASQoSPortQueueShaingPercentage,
       "hwBRASQoSPortQueuePortWredName": hwBRASQoSPortQueuePortWredName,
       "hwBRASQoSPortQueueRowStatus": hwBRASQoSPortQueueRowStatus,
       "hwBRASQoSPortWredTable": hwBRASQoSPortWredTable,
       "hwBRASQoSPortWredEntry": hwBRASQoSPortWredEntry,
       "hwBRASQoSPortWredName": hwBRASQoSPortWredName,
       "hwBRASQoSPortWredGreenLowLimitValue": hwBRASQoSPortWredGreenLowLimitValue,
       "hwBRASQoSPortWredGreenHighLimitValue": hwBRASQoSPortWredGreenHighLimitValue,
       "hwBRASQoSPortWredGreenDiscardValue": hwBRASQoSPortWredGreenDiscardValue,
       "hwBRASQoSPortWredYellowLowLimitValue": hwBRASQoSPortWredYellowLowLimitValue,
       "hwBRASQoSPortWredYellowHighLimitValue": hwBRASQoSPortWredYellowHighLimitValue,
       "hwBRASQoSPortWredYellowDiscardValue": hwBRASQoSPortWredYellowDiscardValue,
       "hwBRASQoSPortWredRedLowLimitValue": hwBRASQoSPortWredRedLowLimitValue,
       "hwBRASQoSPortWredRedHighLimitValue": hwBRASQoSPortWredRedHighLimitValue,
       "hwBRASQoSPortWredRedDiscardValue": hwBRASQoSPortWredRedDiscardValue,
       "hwBRASQoSPortWredRowStatus": hwBRASQoSPortWredRowStatus,
       "hwBRASQoSCarProfileTable": hwBRASQoSCarProfileTable,
       "hwBRASQoSCarProfileEntry": hwBRASQoSCarProfileEntry,
       "hwBRASQoSCarProfileIndex": hwBRASQoSCarProfileIndex,
       "hwBRASQoSCarProfileName": hwBRASQoSCarProfileName,
       "hwBRASQoSCarProfileCir": hwBRASQoSCarProfileCir,
       "hwBRASQoSCarProfilePir": hwBRASQoSCarProfilePir,
       "hwBRASQoSCarProfileCbs": hwBRASQoSCarProfileCbs,
       "hwBRASQoSCarProfilePbs": hwBRASQoSCarProfilePbs,
       "hwBRASQoSCarProfileRowStatus": hwBRASQoSCarProfileRowStatus,
       "hwBRASQoSSlotTable": hwBRASQoSSlotTable,
       "hwBRASQoSSlotEntry": hwBRASQoSSlotEntry,
       "hwBRASQoSSlotId": hwBRASQoSSlotId,
       "hwBRASQoSSlotLinkLayerExclude": hwBRASQoSSlotLinkLayerExclude,
       "hwBRASQoSSlotEtherAjustOverhead": hwBRASQoSSlotEtherAjustOverhead,
       "hwBRASQoSSlotRemoteAdjustEnableStatus": hwBRASQoSSlotRemoteAdjustEnableStatus,
       "hwBRASQoSSlotInboundGqUsedNum": hwBRASQoSSlotInboundGqUsedNum,
       "hwBRASQoSSlotInboundSqUsedNum": hwBRASQoSSlotInboundSqUsedNum,
       "hwBRASQoSSlotInboundGqFreeNum": hwBRASQoSSlotInboundGqFreeNum,
       "hwBRASQoSSlotInboundSqFreeNum": hwBRASQoSSlotInboundSqFreeNum,
       "hwBRASQoSSlotOutboundGqUsedNum": hwBRASQoSSlotOutboundGqUsedNum,
       "hwBRASQoSSlotOutboundSqUsedNum": hwBRASQoSSlotOutboundSqUsedNum,
       "hwBRASQoSSlotOutboundGqFreeNum": hwBRASQoSSlotOutboundGqFreeNum,
       "hwBRASQoSSlotOutboundSqFreeNum": hwBRASQoSSlotOutboundSqFreeNum,
       "hwBRASQoSSlotActiveStatus": hwBRASQoSSlotActiveStatus,
       "hwBRASQoSMultiShapingTable": hwBRASQoSMultiShapingTable,
       "hwBRASQoSMultiShapingEntry": hwBRASQoSMultiShapingEntry,
       "hwBRASQoSMultiShapingIndex": hwBRASQoSMultiShapingIndex,
       "hwBRASQoSMultiShapingName": hwBRASQoSMultiShapingName,
       "hwBRASQoSMultiShapingEndIndex": hwBRASQoSMultiShapingEndIndex,
       "hwBRASQoSMultiShapingCir": hwBRASQoSMultiShapingCir,
       "hwBRASQoSMultiShapingPir": hwBRASQoSMultiShapingPir,
       "hwBRASQoSMultiShapingQueueLength": hwBRASQoSMultiShapingQueueLength,
       "hwBRASQoSMultiShapingRowStatus": hwBRASQoSMultiShapingRowStatus,
       "hwBRASQoSMibTrap": hwBRASQoSMibTrap,
       "hwBRASQoSTrapOid": hwBRASQoSTrapOid,
       "hwBRASQoSTrapSlotID": hwBRASQoSTrapSlotID,
       "hwBRASQoSFailBandwidth": hwBRASQoSFailBandwidth,
       "hwBRASQoSTrapUserBehavior": hwBRASQoSTrapUserBehavior,
       "hwBRASQoSTrapUserID": hwBRASQoSTrapUserID,
       "hwBRASQoSTrapTunnelID": hwBRASQoSTrapTunnelID,
       "hwBRASQoSTrapQinqVlan": hwBRASQoSTrapQinqVlan,
       "hwBRASQoSTrapVlan": hwBRASQoSTrapVlan,
       "hwBRASQoSTrapIfindex": hwBRASQoSTrapIfindex,
       "hwBRASQoSTrapDefine": hwBRASQoSTrapDefine,
       "hwBRASQoSTraps": hwBRASQoSTraps,
       "hwBRASQoSIfResFail": hwBRASQoSIfResFail,
       "hwBRASQoSIfVlanResFail": hwBRASQoSIfVlanResFail,
       "hwBRASQoSTunnelResFail": hwBRASQoSTunnelResFail,
       "hwBRASQoSUserResFail": hwBRASQoSUserResFail,
       "hwBRASQoSTrunkFail": hwBRASQoSTrunkFail,
       "hwBRASQoSUserBandwidthOverflow": hwBRASQoSUserBandwidthOverflow,
       "hwBRASQoSTMExcepion": hwBRASQoSTMExcepion,
       "hwBrasQosConformance": hwBrasQosConformance,
       "hwBrasQosCompliances": hwBrasQosCompliances,
       "hwBrasQosCompliance": hwBrasQosCompliance,
       "hwBrasQosGroups": hwBrasQosGroups,
       "hwBrasQosQosProfileGroup": hwBrasQosQosProfileGroup,
       "hwBrasQosSchedulerProfileGroup": hwBrasQosSchedulerProfileGroup,
       "hwBrasQosDropProfileGroup": hwBrasQosDropProfileGroup,
       "hwBrasQosQueueProfileGroup": hwBrasQosQueueProfileGroup,
       "hwBrasQosQueueClassGroup": hwBrasQosQueueClassGroup,
       "hwBrasQosFlowMappingGroup": hwBrasQosFlowMappingGroup,
       "hwBrasQosIfGroup": hwBrasQosIfGroup,
       "hwBrasQosIfVcGroup": hwBrasQosIfVcGroup,
       "hwBrasQosVpGroupGroup": hwBrasQosVpGroupGroup,
       "hwBrasQosVcGroupGroup": hwBrasQosVcGroupGroup,
       "hwBrasQosGVpGroupGroup": hwBrasQosGVpGroupGroup,
       "hwBrasQosServiceGroupGroup": hwBrasQosServiceGroupGroup,
       "hwBrasQosPortQueueGroup": hwBrasQosPortQueueGroup,
       "hwBrasQosPortWredGroup": hwBrasQosPortWredGroup,
       "hwBrasQosCarProfileGroup": hwBrasQosCarProfileGroup,
       "hwBrasQosSlotGroup": hwBrasQosSlotGroup,
       "hwBrasQosMultiShapingGroup": hwBrasQosMultiShapingGroup,
       "hwBrasQosTrapOidGroup": hwBrasQosTrapOidGroup,
       "hwBrasQosTrapDefineGroup": hwBrasQosTrapDefineGroup}
)
