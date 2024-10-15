# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:53 2024
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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComRoutePolicy_ObjectIdentity = ObjectIdentity
a3ComRoutePolicy = _A3ComRoutePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23)
)
_A3ComRoutePolicyTable_Object = MibTable
a3ComRoutePolicyTable = _A3ComRoutePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1)
)
if mibBuilder.loadTexts:
    a3ComRoutePolicyTable.setStatus("mandatory")
_A3ComRoutePolicyEntry_Object = MibTableRow
a3ComRoutePolicyEntry = _A3ComRoutePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1)
)
a3ComRoutePolicyEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB", "a3ComRoutePolicyIndex"),
)
if mibBuilder.loadTexts:
    a3ComRoutePolicyEntry.setStatus("mandatory")


class _A3ComRoutePolicyIndex_Type(Integer32):
    """Custom type a3ComRoutePolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_A3ComRoutePolicyIndex_Type.__name__ = "Integer32"
_A3ComRoutePolicyIndex_Object = MibTableColumn
a3ComRoutePolicyIndex = _A3ComRoutePolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 1),
    _A3ComRoutePolicyIndex_Type()
)
a3ComRoutePolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRoutePolicyIndex.setStatus("mandatory")


class _A3ComRoutePolicyProtocolType_Type(Integer32):
    """Custom type a3ComRoutePolicyProtocolType based on Integer32"""
    defaultValue = 1

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("at-aurp", 9),
          ("at-kip", 8),
          ("at-rtmp", 7),
          ("ip-bgp4", 4),
          ("ip-ospf", 3),
          ("ip-rip", 2),
          ("ipx-rip", 5),
          ("ipx-sap", 6),
          ("undefined", 1))
    )


_A3ComRoutePolicyProtocolType_Type.__name__ = "Integer32"
_A3ComRoutePolicyProtocolType_Object = MibTableColumn
a3ComRoutePolicyProtocolType = _A3ComRoutePolicyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 2),
    _A3ComRoutePolicyProtocolType_Type()
)
a3ComRoutePolicyProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyProtocolType.setStatus("mandatory")


class _A3ComRoutePolicyType_Type(Integer32):
    """Custom type a3ComRoutePolicyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_A3ComRoutePolicyType_Type.__name__ = "Integer32"
_A3ComRoutePolicyType_Object = MibTableColumn
a3ComRoutePolicyType = _A3ComRoutePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 3),
    _A3ComRoutePolicyType_Type()
)
a3ComRoutePolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyType.setStatus("mandatory")


class _A3ComRoutePolicyOriginProtocol_Type(Integer32):
    """Custom type a3ComRoutePolicyOriginProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_A3ComRoutePolicyOriginProtocol_Type.__name__ = "Integer32"
_A3ComRoutePolicyOriginProtocol_Object = MibTableColumn
a3ComRoutePolicyOriginProtocol = _A3ComRoutePolicyOriginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 4),
    _A3ComRoutePolicyOriginProtocol_Type()
)
a3ComRoutePolicyOriginProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyOriginProtocol.setStatus("mandatory")


class _A3ComRoutePolicySourceAddress_Type(DisplayString):
    """Custom type a3ComRoutePolicySourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_A3ComRoutePolicySourceAddress_Type.__name__ = "DisplayString"
_A3ComRoutePolicySourceAddress_Object = MibTableColumn
a3ComRoutePolicySourceAddress = _A3ComRoutePolicySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 5),
    _A3ComRoutePolicySourceAddress_Type()
)
a3ComRoutePolicySourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicySourceAddress.setStatus("mandatory")


class _A3ComRoutePolicyRouteAddress_Type(DisplayString):
    """Custom type a3ComRoutePolicyRouteAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_A3ComRoutePolicyRouteAddress_Type.__name__ = "DisplayString"
_A3ComRoutePolicyRouteAddress_Object = MibTableColumn
a3ComRoutePolicyRouteAddress = _A3ComRoutePolicyRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 6),
    _A3ComRoutePolicyRouteAddress_Type()
)
a3ComRoutePolicyRouteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyRouteAddress.setStatus("mandatory")


class _A3ComRoutePolicyRouteMask_Type(DisplayString):
    """Custom type a3ComRoutePolicyRouteMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_A3ComRoutePolicyRouteMask_Type.__name__ = "DisplayString"
_A3ComRoutePolicyRouteMask_Object = MibTableColumn
a3ComRoutePolicyRouteMask = _A3ComRoutePolicyRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 7),
    _A3ComRoutePolicyRouteMask_Type()
)
a3ComRoutePolicyRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyRouteMask.setStatus("mandatory")


class _A3ComRoutePolicyAction_Type(Integer32):
    """Custom type a3ComRoutePolicyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_A3ComRoutePolicyAction_Type.__name__ = "Integer32"
_A3ComRoutePolicyAction_Object = MibTableColumn
a3ComRoutePolicyAction = _A3ComRoutePolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 8),
    _A3ComRoutePolicyAction_Type()
)
a3ComRoutePolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyAction.setStatus("mandatory")


class _A3ComRoutePolicyAdjustMetric_Type(Integer32):
    """Custom type a3ComRoutePolicyAdjustMetric based on Integer32"""
    defaultValue = 1

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
        *(("add", 2),
          ("divide", 5),
          ("module", 6),
          ("multiply", 4),
          ("noop", 1),
          ("subtract", 3))
    )


_A3ComRoutePolicyAdjustMetric_Type.__name__ = "Integer32"
_A3ComRoutePolicyAdjustMetric_Object = MibTableColumn
a3ComRoutePolicyAdjustMetric = _A3ComRoutePolicyAdjustMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 9),
    _A3ComRoutePolicyAdjustMetric_Type()
)
a3ComRoutePolicyAdjustMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyAdjustMetric.setStatus("mandatory")


class _A3ComRoutePolicyMetric_Type(Integer32):
    """Custom type a3ComRoutePolicyMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComRoutePolicyMetric_Type.__name__ = "Integer32"
_A3ComRoutePolicyMetric_Object = MibTableColumn
a3ComRoutePolicyMetric = _A3ComRoutePolicyMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 10),
    _A3ComRoutePolicyMetric_Type()
)
a3ComRoutePolicyMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyMetric.setStatus("mandatory")


class _A3ComRoutePolicyWeight_Type(Integer32):
    """Custom type a3ComRoutePolicyWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_A3ComRoutePolicyWeight_Type.__name__ = "Integer32"
_A3ComRoutePolicyWeight_Object = MibTableColumn
a3ComRoutePolicyWeight = _A3ComRoutePolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 11),
    _A3ComRoutePolicyWeight_Type()
)
a3ComRoutePolicyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyWeight.setStatus("mandatory")


class _A3ComRoutePolicyExportType_Type(Integer32):
    """Custom type a3ComRoutePolicyExportType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("ip-ospf-type1", 1),
          ("ip-ospf-type2", 2))
    )


_A3ComRoutePolicyExportType_Type.__name__ = "Integer32"
_A3ComRoutePolicyExportType_Object = MibTableColumn
a3ComRoutePolicyExportType = _A3ComRoutePolicyExportType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 12),
    _A3ComRoutePolicyExportType_Type()
)
a3ComRoutePolicyExportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyExportType.setStatus("mandatory")
_A3ComRoutePolicyRowStatus_Type = RowStatus
_A3ComRoutePolicyRowStatus_Object = MibTableColumn
a3ComRoutePolicyRowStatus = _A3ComRoutePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 1, 1, 13),
    _A3ComRoutePolicyRowStatus_Type()
)
a3ComRoutePolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyRowStatus.setStatus("mandatory")


class _A3ComRoutePolicyNextFreeIndex_Type(Integer32):
    """Custom type a3ComRoutePolicyNextFreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_A3ComRoutePolicyNextFreeIndex_Type.__name__ = "Integer32"
_A3ComRoutePolicyNextFreeIndex_Object = MibScalar
a3ComRoutePolicyNextFreeIndex = _A3ComRoutePolicyNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 2),
    _A3ComRoutePolicyNextFreeIndex_Type()
)
a3ComRoutePolicyNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRoutePolicyNextFreeIndex.setStatus("mandatory")
_A3ComRoutePolicyIpIfTable_Object = MibTable
a3ComRoutePolicyIpIfTable = _A3ComRoutePolicyIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 3)
)
if mibBuilder.loadTexts:
    a3ComRoutePolicyIpIfTable.setStatus("mandatory")
_A3ComRoutePolicyIpIfEntry_Object = MibTableRow
a3ComRoutePolicyIpIfEntry = _A3ComRoutePolicyIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 3, 1)
)
a3ComRoutePolicyIpIfEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB", "a3ComRoutePolicyIpIfIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB", "a3ComRoutePolicyIpIfAddressIndex"),
)
if mibBuilder.loadTexts:
    a3ComRoutePolicyIpIfEntry.setStatus("mandatory")


class _A3ComRoutePolicyIpIfIndex_Type(Integer32):
    """Custom type a3ComRoutePolicyIpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_A3ComRoutePolicyIpIfIndex_Type.__name__ = "Integer32"
_A3ComRoutePolicyIpIfIndex_Object = MibTableColumn
a3ComRoutePolicyIpIfIndex = _A3ComRoutePolicyIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 3, 1, 1),
    _A3ComRoutePolicyIpIfIndex_Type()
)
a3ComRoutePolicyIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRoutePolicyIpIfIndex.setStatus("mandatory")
_A3ComRoutePolicyIpIfAddressIndex_Type = IpAddress
_A3ComRoutePolicyIpIfAddressIndex_Object = MibTableColumn
a3ComRoutePolicyIpIfAddressIndex = _A3ComRoutePolicyIpIfAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 3, 1, 2),
    _A3ComRoutePolicyIpIfAddressIndex_Type()
)
a3ComRoutePolicyIpIfAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRoutePolicyIpIfAddressIndex.setStatus("mandatory")
_A3ComRoutePolicyIpIfRowStatus_Type = RowStatus
_A3ComRoutePolicyIpIfRowStatus_Object = MibTableColumn
a3ComRoutePolicyIpIfRowStatus = _A3ComRoutePolicyIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 23, 3, 1, 3),
    _A3ComRoutePolicyIpIfRowStatus_Type()
)
a3ComRoutePolicyIpIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRoutePolicyIpIfRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComRoutePolicy": a3ComRoutePolicy,
       "a3ComRoutePolicyTable": a3ComRoutePolicyTable,
       "a3ComRoutePolicyEntry": a3ComRoutePolicyEntry,
       "a3ComRoutePolicyIndex": a3ComRoutePolicyIndex,
       "a3ComRoutePolicyProtocolType": a3ComRoutePolicyProtocolType,
       "a3ComRoutePolicyType": a3ComRoutePolicyType,
       "a3ComRoutePolicyOriginProtocol": a3ComRoutePolicyOriginProtocol,
       "a3ComRoutePolicySourceAddress": a3ComRoutePolicySourceAddress,
       "a3ComRoutePolicyRouteAddress": a3ComRoutePolicyRouteAddress,
       "a3ComRoutePolicyRouteMask": a3ComRoutePolicyRouteMask,
       "a3ComRoutePolicyAction": a3ComRoutePolicyAction,
       "a3ComRoutePolicyAdjustMetric": a3ComRoutePolicyAdjustMetric,
       "a3ComRoutePolicyMetric": a3ComRoutePolicyMetric,
       "a3ComRoutePolicyWeight": a3ComRoutePolicyWeight,
       "a3ComRoutePolicyExportType": a3ComRoutePolicyExportType,
       "a3ComRoutePolicyRowStatus": a3ComRoutePolicyRowStatus,
       "a3ComRoutePolicyNextFreeIndex": a3ComRoutePolicyNextFreeIndex,
       "a3ComRoutePolicyIpIfTable": a3ComRoutePolicyIpIfTable,
       "a3ComRoutePolicyIpIfEntry": a3ComRoutePolicyIpIfEntry,
       "a3ComRoutePolicyIpIfIndex": a3ComRoutePolicyIpIfIndex,
       "a3ComRoutePolicyIpIfAddressIndex": a3ComRoutePolicyIpIfAddressIndex,
       "a3ComRoutePolicyIpIfRowStatus": a3ComRoutePolicyIpIfRowStatus}
)
